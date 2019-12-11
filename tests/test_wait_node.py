import unittest
from apidaze.script.nodes.wait import Wait
from lxml import etree


class TestWait(unittest.TestCase):
    def test_wait(self):
        expected = "<Wait>5</Wait>"

        node = Wait(5)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
