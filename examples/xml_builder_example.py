from apidaze.xmlbuilder import XMLBuilder
from apidaze.xmlbuilder.nodes.record import Record
from apidaze.xmlbuilder.nodes.dial import Dial, DialStrategy, DialTargetType
from apidaze.xmlbuilder.nodes.answer import Answer
from apidaze.xmlbuilder.nodes.playback import Playback
from apidaze.xmlbuilder.nodes.ringback import Ringback
from apidaze.xmlbuilder.nodes.echo import Echo
from apidaze.xmlbuilder.nodes.hangup import Hangup
from apidaze.xmlbuilder.nodes.intercept import Intercept
from apidaze.xmlbuilder.nodes.speak import Speak, SpeakLanguages
from apidaze.xmlbuilder.nodes.bind import Bind
from apidaze.xmlbuilder.nodes.wait import Wait
from lxml import etree


xml_builder = XMLBuilder()
child = Record(name='my_recording.wav')
child2 = Dial(target_type=DialTargetType.number, destination='4912345567889')
child3 = Answer()
child4 = Playback('my_wav.wav')
child5 = Ringback('http://ring.back')
child6 = Echo(500)
child7 = Hangup()
child8 = Intercept('f28a3e29-dac4-462c-bf94-b1d518ddbe2d')
child9 = Speak(text="Dzień dobry", lang=SpeakLanguages.pl_PL)
child10 = Bind(action='http://script', text="1")
child11 = Wait(5)
child12 = Dial(
    target_type=DialTargetType.sipaccount,
    destination='blabla@blabla.com',
    strategy=DialStrategy.sequence,
    timeout=120)

xml_builder.add(child).add(child2).add(child3).add(child4).add(child5).add(
    child6
    ).add(child7).add(child8).add(child9).add(
        child10
    ).add(child11).add(child12)

s = etree.tostring(xml_builder.root, pretty_print=True)
print(f'{s}')