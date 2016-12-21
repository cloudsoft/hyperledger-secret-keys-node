#!/usr/bin/env python

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from urlparse import urlparse, parse_qs

SECRET_KEYS = ["MwYpmSRjupbT", "5wgHK9qqYaPy", "vQelbRvja7cJ", "9LKqKH5peurL", "Pqh90CEW5juZ", "FfdvDkAdY81P", "QiXJgHyV4t7A", "twoKZouEyLyB", "BxP7QNh778gI", "wu3F1EwJWHvQ"]

class SecretKeysNodeHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        global SECRET_KEYS

        self.send_response(200)
        self.send_header("Content-type:", "text/plain")

        queries = parse_qs(urlparse(self.path).query)
        index = int(queries["index"][0])
        secret_key = SECRET_KEYS[index]

        self.wfile.write("\n")
        self.wfile.write(secret_key)

def main():
    server = HTTPServer(("0.0.0.0", 9999), SecretKeysNodeHandler)
    server.serve_forever()

if __name__ == "__main__":
    main()
