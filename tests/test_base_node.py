import unittest
from apidaze.script.nodes.base_node import BaseNode
from lxml import etree


class TestBaseNode(unittest.TestCase):
    def test_base_node(self):
        expected = "<basenode/>"

        node = BaseNode()
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)

    def test_base_node_bool_value(self):
        node = BaseNode()
        value = node.bool_value(mybool=True)
        self.assertEqual('true', value)

        value = node.bool_value(mybool=False)
        self.assertEqual('false', value)
