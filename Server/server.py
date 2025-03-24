import http.server
import socketserver

PORT = 8000
DIRECTORIO = "."

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Sirviendo en el puerto {PORT}")
    print("Accede desde tu tablet a: http://192.168.213.47:8000")
    httpd.serve_forever()