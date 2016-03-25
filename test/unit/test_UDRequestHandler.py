from mock import MagicMock
from mock import patch as _patch
from mock import sentinel as _sentinel

import pytest as _pytest
import requests

from udplugin.UDRequestHandler import UDRequestHandler


@_pytest.fixture
def rh():
    """Our fixture for all the UDRequestHandler tests."""
    requests = MagicMock(name='requests')
    requests.__repr__.return_value = 'requests'
    return UDRequestHandler(requests)


##################
# dunder methods #
##################

def test___init__():
    """Test request handler is stored correctly and that

       the base_url is a non-empty string.
    """
    request_handler = UDRequestHandler(_sentinel.requests)

    assert request_handler.requests is _sentinel.requests, (
        'Passed in requests object was not assigned to the requests instance '
        'variable.'
        )
    assert isinstance(request_handler.base_url, str), (
        'base_url is not a string.'
        )
    assert request_handler.base_url, 'base_url is the empty string.'


def test___repr__(rh):
    """Test the representation of UDRequest handler correctly uses the

        representation of the request object that it encapsulates.
    """
    rep = repr(rh)
    assert rp == 'UDRequestHandler(requests)', (
        'UDRequestHandler outputs the incorrect representation '
        'format: {}.'.format(rep)
        )


@_patch(UDRequestHandler, 'search', return_value=_sentinel.search)
def test___call__(search, rh):
    """Test that the call routine calls the search functionality."""
    assert callable(rh)
    assert rh(_sentinel.term) == _sentinel.search, (
        'The search function was not properly patched.'
        )
    search.assert_called_once_with(_sentinel.term, (
        'The __call__ method did not call search with the passed in '
        'arguments.'
        )
        )


##########
# search #
##########

@_patch('requests.get', return_value=_sentinel.response)
def test_search(get, rh):
    pass


def test_search_raises_UDError():
    """Test that the search function throws a UDError when verify_record finds

       an invalid record.
    """
    pass


######################
# response_to_record #
######################

def test_response_to_record():
    pass


def test_response_to_record_raises_KeyError():
    """Test that the response_to_record function throws a key error when the

       list attributes which denotes the list of all definitions can not be
       found.
    """
    pass
