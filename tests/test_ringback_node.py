import unittest
from apidaze.script.nodes.ringback import Ringback
from lxml import etree


class TestRingback(unittest.TestCase):
    def test_ringback(self):
        expected = "<Ringback>http://ring.back</Ringback>"

        node = Ringback(file='http://ring.back')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
