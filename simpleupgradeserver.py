"""Simple Upgrade Server
"""

__version__ = "0.1"
__all__ = ["SimpleUpgradeRequestHandler"]

from http.server import SimpleHTTPRequestHandler, BaseHTTPRequestHandler, \
                    HTTPServer
import argparse
import sys

class SimpleUpgradeRequestHandler(SimpleHTTPRequestHandler):
    """Simple upgrade server

    """
    def send_head(self):
        """Common code for GET and HEAD
        """
        print("path = ", self.path)
        code = self.path.split('?',1)[1];
        print("code1 = ", code)
        code = code.rstrip("/")
        print("code2 = ", code)
        if code is "1":
            return super().send_head()
        else:
            return None
    #def send_head(self):
    #    return super().send_head()


def test(HandlerClass=BaseHTTPRequestHandler,
         ServerClass=HTTPServer, protocol="HTTP/1.0", port=8000, bind=""):
    """Test the HTTP request handler class.

    This runs an HTTP server on port 8000 (or the first command line
    argument).

    """
    server_address = (bind, port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received, exiting.")
        httpd.server_close()
        sys.exit(0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', '-b', default='', metavar='ADDRESS',
                        help='Specify alternate bind address '
                             '[default: all interfaces]')
    parser.add_argument('port', action='store',
                        default=8000, type=int,
                        nargs='?',
                        help='Specify alternate port [default: 8000]')
    args = parser.parse_args()
    handler_class = SimpleUpgradeRequestHandler
    test(HandlerClass=handler_class, port=args.port, bind=args.bind)
