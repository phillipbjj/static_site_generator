import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_single(self):
        node = HTMLNode(props={"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")
        
    def test_props_to_html_multiple(self):
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank"
        })
        # Note: Dictionary order is not guaranteed, so we check for both possible orderings
        result = node.props_to_html()
        valid_outputs = [
            ' href="https://www.google.com" target="_blank"',
            ' target="_blank" href="https://www.google.com"'
        ]
        self.assertIn(result, valid_outputs)
        
    def test_repr(self):
        node = HTMLNode("p", "Hello", None, {"class": "greeting"})
        expected = "HTMLNode(tag=p, value=Hello, children=None, props={'class': 'greeting'})"
        self.assertEqual(repr(node), expected)