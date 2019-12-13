from apidaze.script import Builder, Record, Answer, Echo, Speak, Wait
from apidaze.script import Bind, SpeakLanguages, Conference, Playback, Ringback


def intro(localurl):
    builder = Builder()
    ringback = Ringback(file='FR')
    wait8 = Wait(8)
    answer = Answer()
    record = Record(name='example_recording')
    wait = Wait(delay=2)
    playback = Playback(file=f'{localurl}/apidazeintro.wav')
    speak = Speak(text='This example script will show you some things you can do with our API')

    builder.add(ringback).add(wait8).add(answer).add(record).add(wait).add(
        playback).add(speak).add(wait)

    speak = Speak(text='Press 1 for an example of text to speech, press 2 to enter an echo line to check voice latency or press 3 to enter a conference.')
    bind1 = Bind(action=f'{localurl}/step1.xml', text='1')
    bind2 = Bind(action=f'{localurl}/step2.xml', text='2')
    bind3 = Bind(action=f'{localurl}/step3.xml', text='3')
    speak.add(bind1).add(bind2).add(bind3)

    builder.add(speak)

    builder.printXML()


def step1():
    builder = Builder()
    speak = Speak(text="Our text to speech leverages Google's cloud APIs to offer the best possible solution")
    wait1 = Wait(delay=1)

    builder.add(speak).add(wait1)

    speak = Speak(text='A wide variety of voices and languages are available.  Here are just a few', lang=SpeakLanguages.en_AU)
    builder.add(speak).add(wait1)

    speak = Speak(lang=SpeakLanguages.fr_FR, text='Je peux parler français')
    builder.add(speak).add(wait1)

    speak = Speak(lang=SpeakLanguages.de_DE, text='Auch deutsch')
    builder.add(speak).add(wait1)

    speak = Speak(lang=SpeakLanguages.ja_JP, text='そして日本人ですら')
    builder.add(speak).add(wait1)

    speak = Speak(text="You can see our documentation for a full list of supported languages and voices for them.  We'll take you back to the menu for now.")
    wait2 = Wait(2)

    builder.add(speak).add(wait2)
    builder.printXML()


def step2():
    builder = Builder()
    speak = Speak(text='You will now be joined to an echo line.')
    echo = Echo()
    builder.add(speak).add(echo)
    builder.printXML()


def step3():
    builder = Builder()
    speak = Speak('You will be entered into a conference call now.  You can initiate more calls to join participants or hangup to leave')
    conf = Conference(room='SDKTestConference')
    builder.add(speak).add(conf)
    builder.printXML()


intro('http://')
step1()
step2()
step3()