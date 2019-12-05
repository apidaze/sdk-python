import unittest
from apidaze.xmlbuilder.nodes.conference import Conference
from lxml import etree


class TestConference(unittest.TestCase):
    def test_conference(self):
        expected = '<Conference>my_room</Conference>'

        node = Conference(room='my_room')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)
