import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode(
            tag="a",
            value="Google",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        html = node.props_to_html()
        self.assertEqual(html, ' href="https://www.google.com" target="_blank"')

    def test_props_to_html_single(self):
        node = HTMLNode(
            tag="img",
            value=None,
            props={"src": "image.png"}
        )
        html = node.props_to_html()
        self.assertEqual(html, ' src="image.png"')

    def test_props_to_html_none(self):
        node = HTMLNode(tag="p", value="Hello", props=None)
        html = node.props_to_html()
        self.assertEqual(html, "")

    def test_repr(self):
        node = HTMLNode(
            tag="span",
            value="Hello",
            children=None,
            props={"class": "highlight"}
        )
        expected = (
            "HTMLNode(tag='span', value='Hello', children=None, props={'class': 'highlight'})"
        )
        self.assertEqual(repr(node), expected)

    def test_repr_with_children(self):
        child = HTMLNode(tag="b", value="Bold", props=None)
        node = HTMLNode(
            tag="span",
            value=None,
            children=[child],
            props=None
        )
        expected = (
            "HTMLNode(tag='span', value=None, children=[HTMLNode(tag='b', value='Bold', children=None, props=None)], props=None)"
        )
        self.assertEqual(repr(node), expected)

if __name__ == "__main__":
    unittest.main()