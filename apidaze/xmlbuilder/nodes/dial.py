from apidaze.xmlbuilder.nodes.base_node import BaseNode
from enum import Enum


class DialStrategy(Enum):
    simultaneous = 'simultaneous'
    sequence = 'sequence'


class DialTargetType(Enum):
    number = 1
    sipaccount = 2
    sipuri = 3


class Number(BaseNode):
    def __init__(self, number: str):
        super().__init__(number)


class Sipaccount(BaseNode):
    def __init__(self, sipaccount: str):
        super().__init__(sipaccount)


class Sipuri(BaseNode):
    def __init__(self, uri: str):
        super().__init__(uri)


class Dial(BaseNode):
    def __init__(
            self,
            destination: str,
            target_type: DialTargetType,
            timeout: int = 60,
            max_call_duration: int = None,
            strategy: DialStrategy = DialStrategy.simultaneous,
            action: str = None,
            answer_url: str = None,
            caller_hangup_url: str = None
            ):
        attrib = {
            'timeout': str(timeout),
            'strategy': strategy.value,
        }

        if max_call_duration:
            attrib.update({
                'max-call-duration': max_call_duration
            })

        if action:
            attrib.update({
                'action': action
            })

        if answer_url:
            attrib.update({
                'answer-url': answer_url
            })

        if caller_hangup_url:
            attrib.update({
                'caller-hangup-url': caller_hangup_url
            })

        if target_type == DialTargetType.number:
            child = Number(destination)
        elif target_type == DialTargetType.sipaccount:
            child = Sipaccount(destination)
        else:
            child = Sipuri(destination)
        super().__init__(child, attrib=attrib)
