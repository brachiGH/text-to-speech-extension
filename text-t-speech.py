import pyttsx3
from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging
import json
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IPAddr = s.getsockname()[0]
s.close()


PORT = 6789


class S(SimpleHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Expose-Headers", "*")
        self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Expose-Headers", "*")
        self.end_headers()

    def do_GET(self):
        print("GET requests are disabled.")
        
    def do_POST(self):
        self._set_response()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself

        json_string = post_data.decode('utf-8')

        json_obj = json.loads(json_string)
        text_to_speech(json_obj["content"])


def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()


def run(server_class=HTTPServer, handler_class=S, port=PORT):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info("serving at port " + str(PORT) + "    " + IPAddr + ":" + str(PORT) + "    http://localhost" + ":" + str(PORT)+"  |  /upload \n")
    httpd.serve_forever()

if __name__ == '__main__':
    from sys import argv
    engine = pyttsx3.init()

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()