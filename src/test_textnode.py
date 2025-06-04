import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_equal_text(self):
        node1 = TextNode("Text A", TextType.BOLD)
        node2 = TextNode("Text B", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_equal_text_type(self):
        node1 = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_url_none_and_value(self):
        node1 = TextNode("Text", TextType.LINK, url=None)
        node2 = TextNode("Text", TextType.LINK, url="http://example.com")
        self.assertNotEqual(node1, node2)

    def test_url_none_default(self):
        node1 = TextNode("Text", TextType.LINK)
        node2 = TextNode("Text", TextType.LINK, url=None)
        self.assertEqual(node1, node2)

    def test_all_properties_equal(self):
        node1 = TextNode("Text", TextType.LINK, url="http://example.com")
        node2 = TextNode("Text", TextType.LINK, url="http://example.com")
        self.assertEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()