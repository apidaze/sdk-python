from lxml import etree
from apidaze.script.nodes.base_node import BaseNode


class Builder():
    def __init__(self):
        self.root = etree.Element('Document')
        self.work = etree.SubElement(self.root, 'Work')

    def add(self, element: BaseNode):
        self.work.append(element)
        return self

    def write_to_file(self, filename: str):
        tree = etree.ElementTree(self.root)
        tree.write(
            filename,
            pretty_print=True,
            xml_declaration=True,
            encoding="utf-8")

    def printXML(self, pretty_print: bool = True, encoding: str = 'utf8'):
        result = etree.tostring(
            self.root,
            xml_declaration=True,
            pretty_print=pretty_print,
            encoding=encoding).decode(encoding)
        print(result)

    def __str__(self, encoding: str = 'utf-8'):
        return etree.tostring(
            self.root,
            xml_declaration=True,
            pretty_print=True,
            encoding=encoding).decode(encoding)
