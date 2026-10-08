# Northguard public-repository discovery metadata

The organization publishes four software research repositories. Their public
discovery metadata is versioned in [`repository-discovery.json`](repository-discovery.json).

The catalog covers **public repositories only**. Do not put private project
names, unpublished repository inventories or unreleased code here.

## Apply through GitHub CLI

With `gh` installed and authenticated as a user allowed to edit these repos:

```bash
gh auth status
python3 tools/sync_repository_discovery.py
python3 tools/sync_repository_discovery.py --apply
```

On Windows use `py` (or `python`) instead of `python3`.

The first invocation is **read-only**, displaying the changes. The second adds
the catalogued topics and fills **only empty** repository descriptions. Existing
topics and nonempty descriptions are preserved. To alter topics on only one
repository, pass `--repo <name>`; to omit description updates, pass
`--topics-only`.

The script authenticates via GitHub CLI and never reads or stores tokens itself.
It refuses to write to a repository that is not public or whose canonical name
differs from the manifest. Changes to GitHub metadata **do not** require a code
commit in the target software repositories.

**CI scope:** unit tests validate the catalog and the requests the script would
send. GitHub Actions does *not* update any repository topics automatically; the
manual `--apply` command is required.

## Editorial approach

Tags name implemented mechanisms, actual research domains, and common discovery
terms. They do not assert production readiness, verified human attribution,
general network evasion, or validated endpoint protection.

The catalog is tied to the current organization slug. If the organization is
renamed during a later rebrand, update the slug in this file before running
the command again.
