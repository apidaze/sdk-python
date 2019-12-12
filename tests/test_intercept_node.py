import unittest
from apidaze.script.nodes.intercept import Intercept
from lxml import etree


class TestIntercept(unittest.TestCase):
    def test_intercept(self):
        expected = "<intercept>uuid</intercept>"

        node = Intercept(uuid='uuid')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
