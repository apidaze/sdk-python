import unittest
from apidaze.xmlbuilder.nodes.intercept import Intercept
from lxml import etree


class TestIntercept(unittest.TestCase):
    def test_intercept(self):
        expected = "<Intercept>uuid</Intercept>"

        node = Intercept(uuid='uuid')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
