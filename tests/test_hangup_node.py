import unittest
from apidaze.script.nodes.hangup import Hangup
from lxml import etree


class TestHangup(unittest.TestCase):
    def test_hangup(self):
        expected = "<Hangup/>"

        node = Hangup()
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
