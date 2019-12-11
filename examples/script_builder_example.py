from apidaze.script import Builder
from apidaze.script.nodes.record import Record
from apidaze.script.nodes.answer import Answer
from apidaze.script.nodes.echo import Echo
from apidaze.script.nodes.hangup import Hangup
from apidaze.script.nodes.speak import Speak
from apidaze.script.nodes.wait import Wait


def example_1():
    xmlbuilder = Builder()
    answer = Answer()
    speak = Speak(text='Thank you for trying our demo. Have an wonderful day!')
    echo = Echo(500)

    xmlbuilder.add(answer).add(speak).add(echo)
    xmlbuilder.printXML()


def example_2():
    xmlbuilder = Builder()
    answer = Answer()
    speak = Speak(text='Thank you for trying our demo. Have an excellent day!')
    record = Record(name='my_recording.wav')
    wait = Wait(delay=5)
    hangup = Hangup()

    xmlbuilder.add(
        answer
    ).add(
        speak
    ).add(
        record
    ).add(
        wait
    ).add(
        hangup
    )
    xmlbuilder.printXML()


example_1()
example_2()
