import unittest
from apidaze.script.nodes.echo import Echo
from lxml import etree


class TestEcho(unittest.TestCase):
    def test_echo(self):
        expected = "<Echo>500</Echo>"

        node = Echo(500)
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
