from lxml import etree, objectify
from enum import Enum


class BaseNode(objectify.ObjectifiedElement):
    def bool_value(self, mybool: bool) -> str:
        return 'true' if mybool else'false'


class Record(BaseNode):
    def __init__(
            self,
            name: str = "",
            on_answered: bool = False,
            aleg: bool = True,
            bleg: bool = True):
        attrib = {
            'name': name,
            'on-answered': self.bool_value(mybool=on_answered),
            'aleg': self.bool_value(mybool=aleg),
            'bleg': self.bool_value(mybool=bleg)
        }
        super().__init__(attrib=attrib)


class DialStrategy(Enum):
    simultaneous = 'simultaneous'
    sequence = 'sequence'


class Dial(BaseNode):
    def __init__(
            self,
            number: str,
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

        super().__init__(number, attrib=attrib)


class Answer(BaseNode):
    def __init__(self):
        super().__init__()


class Playback(BaseNode):
    def __init__(self, file: str):
        super().__init__(file)


class Ringback(BaseNode):
    def __init__(self, file: str):
        super().__init__(file)


class Echo(BaseNode):
    def __init__(self, delay: int):
        super().__init__(str(delay))


class Hangup(BaseNode):
    def __init__(self):
        super().__init__()


class Intercept(BaseNode):
    def __init__(self, uuid: str):
        super().__init__(uuid)


class SpeakLanguages(Enum):
    default = "en-US"
    en_US = "en-US"
    fr_FR = "fr-FR"
    it_IT = "it-IT"
    es_ES = "es-ES"
    da_DK = "da-DK"
    nl_NL = "nl-NL"
    ja_JP = "ja-JP"
    nb_NO = "nb-NO"
    pt_BR = "pt-BR"
    sk_SK = "sk-SK"
    sv_SE = "sv-SE"
    uk_UA = "uk-UA"
    en_AU = "en-AU"
    en_GB = "en-GB"
    fr_CA = "fr-CA"
    de_DE = "de-DE"
    ko_KR = "ko-KR"
    pl_PL = "pl-PL"
    pt_PT = "pt-PT"
    ru_RU = "ru-RU"
    tr_TR = "tr-TR"


class Speak(BaseNode):
    def __init__(self,
            lang: SpeakLanguages = SpeakLanguages.default,
            text: str
            ):
        attrib = {
            'lang': lang.value,
        }
        super().__init__(text, attrib=attrib)


class XMLBuilder():
    def __init__(self):
        self.root = etree.Element('Document')
        self.work = etree.SubElement(self.root, 'Work')

    def add(self, element: BaseNode):
        self.work.append(element)
        return self


xml_builder = XMLBuilder()
child = Record(name='my_recording.wav')
child2 = Dial(number='4912345567889')
child3 = Answer()
child4 = Playback('my_wav.wav')
child5 = Ringback('http://ring.back')
child6 = Echo(500)
child7 = Hangup()
child8 = Intercept('f28a3e29-dac4-462c-bf94-b1d518ddbe2d')
child9 = Speak(lang=SpeakLanguages.pl_PL, text="Dzień dobry")
xml_builder.add(child).add(child2).add(child3).add(child4).add(child5).add(
    child6
    ).add(child7).add(child8).add(child9)

s = etree.tostring(xml_builder.root, method='xml')
print(s)
