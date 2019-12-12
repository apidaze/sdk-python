from lxml import etree
from apidaze.script.nodes.base_node import BaseNode
from apidaze.script.nodes.answer import Answer # NOQA
from apidaze.script.nodes.bind import Bind # NOQA
from apidaze.script.nodes.conference import Conference # NOQA
from apidaze.script.nodes.dial import Dial # NOQA
from apidaze.script.nodes.echo import Echo # NOQA
from apidaze.script.nodes.hangup import Hangup # NOQA
from apidaze.script.nodes.intercept import Intercept # NOQA
from apidaze.script.nodes.playback import Playback # NOQA
from apidaze.script.nodes.record import Record # NOQA
from apidaze.script.nodes.ringback import Ringback # NOQA
from apidaze.script.nodes.speak import Speak # NOQA
from apidaze.script.nodes.wait import Wait # NOQA


class Builder():
    def __init__(self):
        self.root = etree.Element('document')
        self.work = etree.SubElement(self.root, 'work')

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
