from apidaze.script import Builder, Dial, DialStrategy, DialTargetType
from http.server import HTTPServer, BaseHTTPRequestHandler


def find_me_or_follow_me(first: str, second: str):
    builder = Builder()
    dial = Dial(
        destination=first,
        timeout=12,
        strategy=DialStrategy.sequence,
        target_type=DialTargetType.number)
    dial.add(
        destination=second,
        target_type=DialTargetType.number)

    builder.add(dial)
    return str(builder)


first_number = '123456788'
second_number = '123456799'


class Handler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(find_me_or_follow_me(
            first_number,
            second_number).encode('utf-8'))


port = 8080

handler = Handler

httpd = HTTPServer(("", port), handler)
httpd.serve_forever()
