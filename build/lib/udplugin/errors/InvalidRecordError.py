from udplugin.errors.UDError import UDError


class InvalidRecordError(UDError):


    def __init__(self):
        super(InvalidRecordError, self).__init__()


    def __repr__(self):
        return 'InvalidRecordError()'


    def __str__(self):
        return 'Wrong number of arguments for the record'
