import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

    def test_leaf_to_html_with_props(self):
        node = LeafNode("img", "alt text", {"src": "img.png", "alt": "alt text"})
        self.assertEqual(node.to_html(), '<img src="img.png" alt="alt text">alt text</img>')

    def test_leaf_to_html_raises_value_error(self):
        with self.assertRaises(ValueError):
            LeafNode("p", None)

    def test_leaf_to_html_empty_string(self):
        node = LeafNode("span", "")
        self.assertEqual(node.to_html(), "<span></span>")

if __name__ == "__main__":
    unittest.main()