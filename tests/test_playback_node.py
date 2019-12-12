import unittest
from apidaze.script.nodes.playback import Playback
from lxml import etree


class TestPlayback(unittest.TestCase):
    def test_playback(self):
        expected = "<playback>my_file.wav</playback>"

        node = Playback(file='my_file.wav')
        result = etree.tostring(node, encoding='utf-8').decode('utf-8')

        self.assertEqual(expected, result)
