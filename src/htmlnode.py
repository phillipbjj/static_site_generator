from textnode import TextNode, TextType
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              #String representing HTML tag 
        self.value = value          #Value of tag
        self.children = children    #List of HTMLNode objects
        self.props = props          #Dictionary of key-value pairs representing attributes of the HTML tag
        
    def to_html(self):
        raise NotImplementedError() #Child classes will override this method to render themselves as HTML
    
    def props_to_html(self):
        if not self.props:
            return ""
        return "".join(f" {key}=\"{value}\"" for key, value in self.props.items())
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("Leaf node must have a value")
        super().__init__(tag=tag, value=value, children=None, props=props)
        
    def to_html(self):
        if not self.value:
            raise ValueError("Leaf node must have a value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if not tag:
            raise ValueError("Parent node must have a tag")
        if not children:
            raise ValueError("Parent node must have a child")
        
        super().__init__(tag=tag, value=None, children=children, props=props)
        
    def to_html(self):
        if not self.tag:
            raise ValueError("Parent node must have a tag")
        if not self.children:
            raise ValueError("Parent node must have children")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"


    
    
    