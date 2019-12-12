import unittest
from apidaze.script import Builder, Answer, Speak, Echo
from lxml import etree


class TestXMLBuilder(unittest.TestCase):
    def test_xml_builder(self):
        expected = "<document><work/></document>"

        xmlbuilder = Builder()
        result = etree.tostring(
            xmlbuilder.root,
            encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)

    def test_xml_builder_example(self):
        expected = """
<document>
<work>
<answer/>
<speak lang="en-US">Hello</speak>
<echo>500</echo>
</work>
</document>
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
