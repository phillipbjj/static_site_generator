import unittest
from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_mixed_nodes(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        )

    def test_nested_parent_nodes(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                    ]
                ),
                ParentNode(
                    "p",
                    [
                        LeafNode("i", "Italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p><b>Bold text</b>Normal text</p><p><i>Italic text</i>Normal text</p></div>"
        )

    def test_parent_with_props(self):
        node = ParentNode(
            "div",
            [LeafNode("p", "Text")],
            {"class": "container", "id": "main"}
        )
        self.assertIn(
            node.to_html(),
            [
                '<div class="container" id="main"><p>Text</p></div>',
                '<div id="main" class="container"><p>Text</p></div>'
            ]
        )

    def test_deeply_nested(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        ParentNode(
                            "div",
                            [LeafNode("p", "Deep text")]
                        )
                    ]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><div><div><p>Deep text</p></div></div></div>"
        )

    def test_no_tag_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("p", "text")])

    def test_no_children_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", [])

    def test_none_children_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_invalid_child_type_raises_attribute_error(self):
        with self.assertRaises(AttributeError):
            node = ParentNode("div", ["not a node"])
            node.to_html()

    def test_single_child(self):
        node = ParentNode("div", [LeafNode("p", "Single child")])
        self.assertEqual(node.to_html(), "<div><p>Single child</p></div>")

    def test_multiple_same_type_children(self):
        node = ParentNode(
            "ul",
            [
                LeafNode("li", "Item 1"),
                LeafNode("li", "Item 2"),
                LeafNode("li", "Item 3")
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
        )

    def test_mixed_leaf_and_parent_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph"),
                ParentNode(
                    "div",
                    [LeafNode("span", "Nested span")]
                )
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><p>Paragraph</p><div><span>Nested span</span></div></div>"
        )