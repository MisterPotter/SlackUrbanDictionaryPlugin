from udplugin.UDRequestHandler import UDRequestHandler

from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.web import RequestHandler


def make_app():
    return Application([
        (r'/', UDRequestHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(5127)
    IOLoop.current().start()
