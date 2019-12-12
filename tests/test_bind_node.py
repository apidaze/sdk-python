import unittest
from apidaze.script.nodes.bind import Bind
from lxml import etree


class TestBind(unittest.TestCase):
    def test_bind(self):
        expected = '<bind action="http://script">1</bind>'

        node = Bind(text='1', action='http://script')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)
