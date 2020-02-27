import unittest
from requests_mock import Mocker
from apidaze.http import Http
from apidaze.mediafiles import Mediafiles


class TestMediafiles(unittest.TestCase):
    @property
    def httpInstance(self):
        return Http(
            api_key='API_KEY',
            api_secret='API_SECRET',
            api_url='http://api.url')

    @property
    def mediafiles(self):
        return Mediafiles(self.httpInstance)

# ['anything.wav', 'lxx9.wav', 'mll.mp3', 'sclft.wav', 'scmo.wav', 'scold.wav', 'scolda.wav', 'scoldu.wav', 'scrgt.wav', 'scst.wav', 'scstlft.wav', 'scstrgt.wav', 'sl.mp3', 'socold.WAV', 'socold.wav', 'stest.wav', 'testFile.wav', 'testa7.wav', 'xx8.wav', 'xx9.wav', 'zzz8.wav'], 'status_code': 200


    @Mocker()
    def prepare_list(self, status_code, mocker):
        body = {
            'body': ['test1.wav', 'test2.wav', 'test3.mp3', 'test4.wav', 'test5.wav'],
            'status_code': status_code
        }

        mocker.register_uri(
            method='GET',
            url=f'{self.httpInstance.base_url}/mediafiles',
            json=body,
            status_code=status_code
        )

        expected_body = {
            'body': body,
            'status_code': status_code
        }

        response = self.mediafiles.list()

        self.assertEqual(expected_body, response)

    def test_list_success(self):
        self.prepare_list(200)

    def test_list_failure(self):
        self.prepare_list(401)
