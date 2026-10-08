#!/usr/bin/env python3
"""Preview or apply public GitHub topics and empty descriptions via the GitHub CLI.

Runs only on explicitly catalogued, public repositories. Existing topics are
preserved; nonempty descriptions are never overwritten.
"""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys

CATALOG = Path(__file__).resolve().parents[1] / "repository-discovery.json"
TOPIC_RE = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,48}[a-z0-9])?$")
REPO_RE = re.compile(r"^[A-Za-z0-9._-]+$")


def load_catalog(path=CATALOG):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    org = data.get("organization")
    if not isinstance(org, str) or not REPO_RE.fullmatch(org):
        raise ValueError("Invalid organization")
    repos = data.get("repositories")
    if not isinstance(repos, list) or not repos:
        raise ValueError("No repositories in catalog")
    seen = set()
    for entry in repos:
        name, topics, desc = entry.get("name"), entry.get("topics"), entry.get("description")
        if not isinstance(name, str) or not REPO_RE.fullmatch(name) or name in seen:
            raise ValueError(f"Invalid or duplicate repository: {name!r}")
        seen.add(name)
        if not isinstance(desc, str) or not 8 <= len(desc) <= 160:
            raise ValueError(f"Invalid description length: {name}")
        if not isinstance(topics, list) or not 1 <= len(topics) <= 20:
            raise ValueError(f"Invalid topic count: {name}")
        if len(topics) != len(set(topics)) or any(
            not isinstance(t, str) or not TOPIC_RE.fullmatch(t) for t in topics
        ):
            raise ValueError(f"Invalid or duplicate topics: {name}")
    return data


def gh_api(method, endpoint, payload=None):
    args = ["gh", "api", "-X", method, endpoint, "-H", "Accept: application/vnd.github+json"]
    if payload is not None:
        args.extend(["--input", "-"])
    completed = subprocess.run(
        args,
        input=json.dumps(payload) if payload is not None else None,
        text=True,
        capture_output=True,
        check=True,
    )
    return json.loads(completed.stdout) if completed.stdout.strip() else {}


def sync_catalog(data, apply=False, only=None, include_descriptions=True):
    org = data["organization"]
    if only:
        unknown = set(only) - {r["name"] for r in data["repositories"]}
        if unknown:
            raise ValueError(f"Unknown repository selection: {', '.join(sorted(unknown))}")

    change_count = 0
    for item in data["repositories"]:
        name = item["name"]
        if only and name not in only:
            continue
        endpoint = f"repos/{org}/{name}"
        remote = gh_api("GET", endpoint)
        if remote.get("full_name") != f"{org}/{name}" or remote.get("private") is not False:
            raise ValueError(f"Repository is not the expected PUBLIC repository: {endpoint}")
        current_topics = remote.get("topics", [])
        if not isinstance(current_topics, list):
            raise ValueError(f"Topic metadata missing: {endpoint}")
        combined = list(dict.fromkeys(current_topics + item["topics"]))
        add = [t for t in combined if t not in current_topics]
        set_description = include_descriptions and not remote.get("description")
        print(f"{endpoint}: +{len(add)} topics, description={'set' if set_description else 'unchanged'}")
        if add:
            print("  add: " + ", ".join(add))
        if apply:
            if add:
                gh_api("PUT", endpoint + "/topics", {"names": combined})
            if set_description:
                gh_api("PATCH", endpoint, {"description": item["description"]})
        change_count += bool(add or set_description)
    return change_count


def main():
    parser = argparse.ArgumentParser(description="Sync public Northguard repository discovery metadata")
    parser.add_argument("--apply", action="store_true", help="Write topics and missing descriptions; default is preview only")
    parser.add_argument("--repo", action="append", help="Only process named catalogued repository (repeatable)")
    parser.add_argument("--topics-only", action="store_true", help="Do not fill missing descriptions")
    parser.add_argument("--catalog", type=Path, default=CATALOG)
    args = parser.parse_args()
    try:
        data = load_catalog(args.catalog)
        count = sync_catalog(data, apply=args.apply, only=args.repo,
                             include_descriptions=not args.topics_only)
        print(f"{'APPLIED' if args.apply else 'PREVIEW'}: {count} repositories need(ed) changes")
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"METADATA_SYNC_ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
