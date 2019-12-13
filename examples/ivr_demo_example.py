from apidaze.script import Builder, Record, Answer, Echo, Speak, Wait
from apidaze.script import Bind, SpeakLanguages, Conference, Playback, Ringback
from http.server import HTTPServer, BaseHTTPRequestHandler


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

    return str(builder)


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
    return str(builder)


def step2():
    builder = Builder()
    speak = Speak(text='You will now be joined to an echo line.')
    echo = Echo()
    builder.add(speak).add(echo)
    return str(builder)


def step3():
    builder = Builder()
    speak = Speak('You will be entered into a conference call now.  You can initiate more calls to join participants or hangup to leave')
    conf = Conference(room='SDKTestConference')
    builder.add(speak).add(conf)
    return str(builder)


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if self.path == '/':
            self.wfile.write(intro('http://localhost').encode('utf-8'))
        elif self.path == '/step1.xml':
            self.wfile.write(step1().encode('utf-8'))
        elif self.path == '/step2.xml':
            self.wfile.write(step2().encode('utf-8'))
        elif self.path == '/step3.xml':
            self.wfile.write(step3().encode('utf-8'))


port = 8080
handler = Handler

httpd = HTTPServer(("", port), handler)
httpd.serve_forever()

