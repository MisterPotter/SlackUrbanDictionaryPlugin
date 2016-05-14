from udplugin.errors.UDError import UDError


class InvalidSearchError(UDError):


    def __init__(self, search_key):
        super(InvalidSearchError, self).__init__()
        self.search_key = search_key


    def __repr__(self):
        return 'InvalidSearchError(%r)' % self.search_key


    def __str__(self):
        return 'Invalid search key: %s' % self.search_key
