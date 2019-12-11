import unittest
from apidaze.script.nodes.dial import DialTargetType, DialStrategy, Dial
from lxml import etree


class TestDial(unittest.TestCase):
    def test_dial_number(self):
        expected = """
<Dial timeout="60" strategy="simultaneous">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous">
<Sipaccount>sip@account</Sipaccount>
</Dial>
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
<Dial timeout="60" strategy="simultaneous">
<Sipuri>sip://uri</Sipuri>
</Dial>
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
<Dial timeout="60" strategy="simultaneous">
<Number>1234567890</Number>
<Number>0000000000</Number>
<Number>1111111111</Number>
</Dial>
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
<Dial timeout="60" strategy="sequence">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="120" strategy="simultaneous">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous" max-call-duration="120">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous" action="http://action">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous" answer-url="http://url">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous" caller-hangup-url="http://url">
<Number>1234567890</Number>
</Dial>
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
<Dial timeout="60" strategy="simultaneous">
<Number>1234567890</Number>
<Sipaccount>sip@account</Sipaccount>
<Sipuri>sip://uri</Sipuri>
</Dial>
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
