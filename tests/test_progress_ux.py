"""Cover regressions against real content: entry point, content counts and personal state."""
import re
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import build

def guide(start=""):
    cfg, _ = build.load_config(ROOT / "tests" / "base-edition.json")
    cfg["book"]["start_chapter"] = start
    return build.Guide(cfg, build.Content(cfg), {"editions": []})

def button(g):
    return re.search(r'<a class="btn btn--dark" href="([^"]+)"', g.view_home()).group(1)

class Cover(unittest.TestCase):
    def test_reading_entry_and_override(self):
        g = guide()
        self.assertEqual(button(g), g.page_href(g.intro["id"]))
        first = g.chapters[0]["id"]
        self.assertIn(g.chapter_href(first, g.built[first]["checklist_id"]), g.view_home())
        g.intro = None
        self.assertEqual(button(g), g.chapter_href(first))
        g = guide("passwords")
        self.assertEqual(button(g), g.chapter_href("passwords"))

    def test_content_is_not_a_completion_score(self):
        g = guide()
        home = g.view_home()
        block = re.search(r'<section class="block" aria-labelledby="preview">.*?</section>', home, re.S).group(0)
        self.assertIn("In this guide", block)
        self.assertIn("18 chapters with 90 checklist actions", block)
        for marker in ('class="stats"', 'data-bar', 'data-stat', '18/18', '90/90'):
            self.assertNotIn(marker, block)
        self.assertNotIn("--share", home)
        self.assertEqual(set(re.findall(r'data-stat="[^"]+">([^<]+)', home)), {"0"})
        entry = next(e for e in g.search_index() if e["href"] == g.home_href("preview"))
        self.assertEqual(entry["title"], "In this guide")

if __name__ == "__main__":
    unittest.main()
