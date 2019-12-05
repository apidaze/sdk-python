import unittest
from apidaze.xmlbuilder.nodes.record import Record
from lxml import etree


class TestRecord(unittest.TestCase):
    def test_record(self):
        expected = """
<Record on-answered="false" aleg="true" bleg="true" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(name='my_recording.wav')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_record_on_answered(self):
        expected = """
<Record on-answered="true" aleg="true" bleg="true" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(
            name='my_recording.wav',
            on_answered=True
            )
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_record_aleg(self):
        expected = """
<Record on-answered="false" aleg="false" bleg="true" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(
            name='my_recording.wav',
            aleg=False
            )
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_record_bleg(self):
        expected = """
<Record on-answered="false" aleg="true" bleg="false" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(
            name='my_recording.wav',
            bleg=False
            )
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_record_aleg_bleg(self):
        expected = """
<Record on-answered="false" aleg="false" bleg="false" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(
            name='my_recording.wav',
            bleg=False,
            aleg=False
            )
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)

    def test_record_all(self):
        expected = """
<Record on-answered="true" aleg="false" bleg="false" name="my_recording.wav"/>
""".replace('\n', '')

        node = Record(
            name='my_recording.wav',
            bleg=False,
            aleg=False,
            on_answered=True
            )
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
