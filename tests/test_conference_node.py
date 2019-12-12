import unittest
from apidaze.script.nodes.conference import Conference
from lxml import etree


class TestConference(unittest.TestCase):
    def test_conference(self):
        expected = '<conference>my_room</conference>'

        node = Conference(room='my_room')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)
