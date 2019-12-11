import unittest
from apidaze.script import Builder
from apidaze.script.nodes.answer import Answer
from apidaze.script.nodes.speak import Speak
from apidaze.script.nodes.echo import Echo
from lxml import etree


class TestXMLBuilder(unittest.TestCase):
    def test_xml_builder(self):
        expected = "<Document><Work/></Document>"

        xmlbuilder = Builder()
        result = etree.tostring(
            xmlbuilder.root,
            encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)

    def test_xml_builder_example(self):
        expected = """
<Document>
<Work>
<Answer/>
<Speak lang="en-US">Hello</Speak>
<Echo>500</Echo>
</Work>
</Document>
""".replace('\n', '')

        xmlbuilder = Builder()
        answer = Answer()
        speak = Speak(text='Hello')
        echo = Echo(500)

        xmlbuilder.add(answer).add(speak).add(echo)

        result = etree.tostring(
            xmlbuilder.root,
            encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)
