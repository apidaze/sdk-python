import unittest
from apidaze.xmlbuilder.nodes.speak import Speak, SpeakLanguages
from lxml import etree


class TestSpeak(unittest.TestCase):
    def test_speak_default(self):
        expected = '<Speak lang="en-US">Hello</Speak>'

        node = Speak(text='Hello')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_pl_PL(self):
        expected = '<Speak lang="pl-PL">Cześć</Speak>'

        node = Speak(text='Cześć', lang=SpeakLanguages.pl_PL)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_de_DE(self):
        expected = '<Speak lang="de-DE">Hallo</Speak>'

        node = Speak(text='Hallo', lang=SpeakLanguages.de_DE)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_US(self):
        expected = '<Speak lang="en-US">Hello</Speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_US)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_GB(self):
        expected = '<Speak lang="en-GB">Hello</Speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_GB)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_AU(self):
        expected = '<Speak lang="en-AU">Hello</Speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_AU)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
