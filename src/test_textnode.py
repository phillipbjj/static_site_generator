import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        
    def test_different_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_different_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_url_equality(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://example.com")
        self.assertEqual(node, node2)
    
    def test_url_difference(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://other.com")
        self.assertNotEqual(node, node2)
    
    def test_none_url(self):
        node = TextNode("Text", TextType.TEXT)
        node2 = TextNode("Text", TextType.TEXT, None)
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()