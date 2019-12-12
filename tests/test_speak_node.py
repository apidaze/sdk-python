import unittest
from apidaze.script.nodes.speak import Speak, SpeakLanguages
from lxml import etree


class Testspeak(unittest.TestCase):
    def test_speak_default(self):
        expected = '<speak lang="en-US">Hello</speak>'

        node = Speak(text='Hello')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_pl_PL(self):
        expected = '<speak lang="pl-PL">Cześć</speak>'

        node = Speak(text='Cześć', lang=SpeakLanguages.pl_PL)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_de_DE(self):
        expected = '<speak lang="de-DE">Hallo</speak>'

        node = Speak(text='Hallo', lang=SpeakLanguages.de_DE)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_US(self):
        expected = '<speak lang="en-US">Hello</speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_US)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_GB(self):
        expected = '<speak lang="en-GB">Hello</speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_GB)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_speak_en_AU(self):
        expected = '<speak lang="en-AU">Hello</speak>'

        node = Speak(text='Hello', lang=SpeakLanguages.en_AU)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
