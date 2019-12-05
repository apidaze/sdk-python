import unittest
from apidaze.xmlbuilder.nodes.bind import Bind
from lxml import etree


class TestBind(unittest.TestCase):
    def test_bind(self):
        expected = '<Bind action="http://script">1</Bind>'

        node = Bind(text='1', action='http://script')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)