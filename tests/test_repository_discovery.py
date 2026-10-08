"""Static and mocked checks: no GitHub metadata is changed in CI."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from tools.sync_repository_discovery import load_catalog, sync_catalog


class CatalogTests(unittest.TestCase):
    def test_only_four_known_public_labs_are_catalogued(self):
        data = load_catalog()
        self.assertEqual(data["organization"], "Northguard-Security")
        names = {r["name"] for r in data["repositories"]}
        self.assertEqual(names, {
            "PAW--Phishing-Attribution-Workbench--",
            "Reverse-Observer",
            "mirage-flow",
            "Chimera",
        })

    def test_invalid_topic_or_duplicate_rejected(self):
        source = load_catalog()
        source["repositories"][0]["topics"].append("Bad Topic")
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.json"
            path.write_text(json.dumps(source), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Invalid or duplicate topics"):
                load_catalog(path)

    def test_preview_does_not_mutate(self):
        data = load_catalog()
        one = data["repositories"][0]
        def fake_api(method, endpoint, payload=None):
            self.assertEqual(method, "GET")
            self.assertEqual(endpoint, f"repos/Northguard-Security/{one['name']}")
            return {
                "full_name": f"Northguard-Security/{one['name']}",
                "private": False,
                "topics": [],
                "description": None,
            }
        with patch("tools.sync_repository_discovery.gh_api", side_effect=fake_api) as api:
            changed = sync_catalog(data, apply=False, only=[one["name"]])
        self.assertEqual(changed, 1)
        self.assertEqual(api.call_count, 1)

    def test_apply_is_additive_and_does_not_overwrite_descriptions(self):
        data = load_catalog()
        one = data["repositories"][0]
        calls = []
        def fake_api(method, endpoint, payload=None):
            calls.append((method, endpoint, payload))
            if method == "GET":
                return {
                    "full_name": f"Northguard-Security/{one['name']}",
                    "private": False,
                    "topics": ["custom-topic", one["topics"][0]],
                    "description": "Existing author description",
                }
            return {}
        with patch("tools.sync_repository_discovery.gh_api", side_effect=fake_api):
            changed = sync_catalog(data, apply=True, only=[one["name"]])
        self.assertEqual(changed, 1)
        self.assertEqual([x[0] for x in calls], ["GET", "PUT"])
        names = calls[1][2]["names"]
        self.assertEqual(names[0], "custom-topic")
        self.assertEqual(names.count(one["topics"][0]), 1)
        self.assertTrue(set(one["topics"]).issubset(set(names)))

    def test_apply_refuses_private_repository(self):
        data = load_catalog()
        one = data["repositories"][0]
        with patch("tools.sync_repository_discovery.gh_api", return_value={
            "full_name": f"Northguard-Security/{one['name']}",
            "private": True,
            "topics": [],
            "description": "",
        }) as api:
            with self.assertRaisesRegex(ValueError, "not the expected PUBLIC repository"):
                sync_catalog(data, apply=True, only=[one["name"]])
        self.assertEqual(api.call_count, 1)

    def test_non_catalogued_repository_cannot_be_targeted(self):
        data = load_catalog()
        with patch("tools.sync_repository_discovery.gh_api") as api:
            with self.assertRaisesRegex(ValueError, "Unknown repository"):
                sync_catalog(data, apply=True, only=["nonexistent"])
        api.assert_not_called()


if __name__ == "__main__":
    unittest.main()
