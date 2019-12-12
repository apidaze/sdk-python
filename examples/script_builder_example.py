from apidaze.script import Builder, Record, Answer, Echo, Hangup, Speak, Wait 
from apidaze.script import Ringback, Bind, SpeakLanguages, Conference


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


def intro():
    builder = Builder()
    answer = Answer()
    record = Record(name='example_recording')
    wait = Wait(delay=2)
    # playback = 
    speak = Speak(text='This example script will show you some things you can do with our API')

    builder.add(answer).add(record).add(wait).add(speak).add(wait)

    speak = Speak(text='Press 1 for an example of text to speech, press 2 to enter an echo line to check voice latency or press 3 to enter a conference.')
    bind1 = Bind(action='http://b.atwa.us/apidaze/step1.xml', text='1')
    bind2 = Bind(action='http://b.atwa.us/apidaze/step2.xml', text='2')
    bind3 = Bind(action='http://b.atwa.us/apidaze/step3.xml', text='3')
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


# example_1()
# example_2()
intro()
step1()
step2()
step3()