import json
import tempfile
import unittest
from pathlib import Path

from settings_store import apply_settings


class SettingsStoreTest(unittest.TestCase):
    def test_updates_top_level_value(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "settings.json"
            path.write_text(json.dumps({"language": "en", "theme": "light"}), encoding="utf-8")

            result = apply_settings(path, {"language": "zh-CN"})

            self.assertEqual(result, {"language": "zh-CN", "theme": "light"})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), result)


if __name__ == "__main__":
    unittest.main()
