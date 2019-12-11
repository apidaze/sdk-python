from apidaze.script.nodes.base_node import BaseNode
from enum import Enum


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
    """
    Say the text enclosed in the tag.

    Parameters
    ----------
    text: str
        Text to be spoken.
    lang: SpeakLanguages
        The language this text will be spoken

    Returns
    -------
    object
        Speak node object
    """
    def __init__(
            self,
            text: str,
            lang: SpeakLanguages = SpeakLanguages.default
            ):
        attrib = {
            'lang': lang.value,
        }
        super().__init__(text, attrib=attrib)
