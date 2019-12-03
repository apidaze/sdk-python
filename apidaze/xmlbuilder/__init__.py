from lxml import etree
from apidaze.xmlbuilder.nodes.base_node import BaseNode


class XMLBuilder():
    def __init__(self):
        self.root = etree.Element('Document')
        self.work = etree.SubElement(self.root, 'Work')

    def add(self, element: BaseNode):
        self.work.append(element)
        return self

