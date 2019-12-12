import unittest
from apidaze.script.nodes.dial import DialTargetType, DialStrategy, Dial
from lxml import etree


class Testdial(unittest.TestCase):
    def test_dial_number(self):
        expected = """
<dial timeout="60" strategy="simultaneous">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_sipaccount(self):
        expected = """
<dial timeout="60" strategy="simultaneous">
<sipaccount>sip@account</sipaccount>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='sip@account',
            target_type=DialTargetType.sipaccount)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_sipuri(self):
        expected = """
<dial timeout="60" strategy="simultaneous">
<sipuri>sip://uri</sipuri>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='sip://uri',
            target_type=DialTargetType.sipuri)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_multiple_numbers(self):
        expected = """
<dial timeout="60" strategy="simultaneous">
<number>1234567890</number>
<number>0000000000</number>
<number>1111111111</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number)
        node.add(destination='0000000000', target_type=DialTargetType.number)
        node.add(destination='1111111111', target_type=DialTargetType.number)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_strategy_sequence(self):
        expected = """
<dial timeout="60" strategy="sequence">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            strategy=DialStrategy.sequence)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_timeout(self):
        expected = """
<dial timeout="120" strategy="simultaneous">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            timeout=120)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_max_call_duration(self):
        expected = """
<dial timeout="60" strategy="simultaneous" max-call-duration="120">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            max_call_duration=120)
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_action(self):
        expected = """
<dial timeout="60" strategy="simultaneous" action="http://action">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            action='http://action')
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_answer_url(self):
        expected = """
<dial timeout="60" strategy="simultaneous" answer-url="http://url">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            answer_url='http://url')
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_(self):
        expected = """
<dial timeout="60" strategy="simultaneous" caller-hangup-url="http://url">
<number>1234567890</number>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number,
            caller_hangup_url='http://url')
        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)

    def test_dial_different_targets(self):
        expected = """
<dial timeout="60" strategy="simultaneous">
<number>1234567890</number>
<sipaccount>sip@account</sipaccount>
<sipuri>sip://uri</sipuri>
</dial>
""".replace('\n', '')

        node = Dial(
            destination='1234567890',
            target_type=DialTargetType.number)
        node.add(
            destination='sip@account',
            target_type=DialTargetType.sipaccount)
        node.add(
            destination='sip://uri',
            target_type=DialTargetType.sipuri)

        result = etree.tostring(
            node,
            encoding='utf-8',
            pretty_print=False).decode('utf-8')

        self.assertEqual(expected, result)
