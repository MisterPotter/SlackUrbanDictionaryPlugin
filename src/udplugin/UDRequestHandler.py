from udplugin.UDRequest import UDRequest

from tornado.web import RequestHandler


class UDRequestHandler(RequestHandler):

    def get(self):
        term = self.get_argument('term')
        ud_request = UDRequest()
        self.write(ud_request(term))
