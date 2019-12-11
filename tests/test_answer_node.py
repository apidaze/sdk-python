import unittest
from apidaze.script.nodes.answer import Answer
from lxml import etree


class TestAnswer(unittest.TestCase):
    def test_answer(self):
        expected = "<Answer/>"

        node = Answer()
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')
        self.assertEqual(expected, result)
