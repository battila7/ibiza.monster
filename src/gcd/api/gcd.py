from http.server import BaseHTTPRequestHandler
import urllib

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()

        o = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(o.query)

        a = int(query['a'][0])
        b = int(query['b'][0])

        self.wfile.write(str(gcd(a, b)).encode())
        
        return
