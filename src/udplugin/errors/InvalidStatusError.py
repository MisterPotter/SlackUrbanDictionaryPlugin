from udplugin.errors.UDError import UDError

class InvalidStatusError(UDError):


    def __init__(self, status):
        super(InvalidStatusError, self).__init__()
        self.status = status


    def __repr__(self):
        return 'InvalidStatusError(%r)' % self.status


    def __str__(self):
        return 'Non successfull status code: %d was returned' % status_code
