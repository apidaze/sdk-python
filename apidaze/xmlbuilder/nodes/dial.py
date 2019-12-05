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
    """
    Place a call to a destination. A destination can be an external number,
    a SIP account or a voicemail box. Multiple destinations can be dialed
    simultaneously or in sequence.

    Parameters
    ----------
    destination: str
        Call destination. Can be number, sipaccount or sipuri.
    target_type: DialTargetType
        Choose from between number, sipaccount or sipuri.
    timeout: int
        The maximum time (in seconds) to ring the call destination.
        Default is 60.
    max_call_duration: int
        The maximum time (in seconds) for this call.
        The corresponding timer starts when the call is answered.
    strategy: DialStrategy
        When dialing multiple destinations, ring them in sequence
        or simultaneously.
    action: str
        The URL of the external script to fetch when the callee
        ends the current call.
    answer_url: str
        A URL containing XML instructions to run on the callee side
        when the callee answers the call, and before establishing
        the call with the caller.
    caller_hangup_url: str
        A URL containing XML instructions to run on the callee
        side when the caller hangs up.

    Returns
    -------
    object
        Dial node object
    """
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
                'max-call-duration': str(max_call_duration)
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

    def add(self,
            destination: str,
            target_type: DialTargetType):
        if target_type == DialTargetType.number:
            child = Number(destination)
        elif target_type == DialTargetType.sipaccount:
            child = Sipaccount(destination)
        else:
            child = Sipuri(destination)
        self.append(child)
        return self
