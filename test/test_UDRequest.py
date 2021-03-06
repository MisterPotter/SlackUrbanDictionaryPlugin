from unittest.mock import MagicMock
from unittest.mock import patch as _patch
from unittest.mock import sentinel as _sentinel

import pytest as _pytest
import requests

from udplugin.UDRequest import UDRequest


@_pytest.fixture
def request():
    """Our fixture for all the UDRequest tests."""
    return UDRequest()


##################
# dunder methods #
##################


def test___repr__(request):
    """Test the representation of UDRequest handler correctly uses the

        representation of the request object that it encapsulates.
    """
    rep = repr(request)
    assert rep == 'UDRequestHandler()', (
        'UDRequestHandler outputs the incorrect representation '
        'format: {}.'.format(rep)
    )


@_patch.object(UDRequest, 'search', return_value=_sentinel.search)
def test___call__(search, request):
    """Test that the call routine calls the search functionality."""
    assert callable(request)
    assert request(_sentinel.term) == _sentinel.search, (
        'The request callable did not return the expected value.'
    )
    search.assert_called_once_with(_sentinel.term)


##########
# search #
##########

@_pytest.mark.xfail
@_patch.object(UDRequest, 'verify_record')
@_patch.object(
    UDRequest, 'response_to_record',
    return_value=_sentinel.ud_record
)
@_patch('udplugin.UDRequest.requests.get', return_value=_sentinel.ud_response)
def test_search(get, response_to_record, verify_record, request):
    """Test the search functionality."""
    assert request.search('nub') == _sentinel.ud_record

    get.assert_called_once_with(
        'http://api.urbandictionary.com/v0/define?term=nub'
    )
    response_to_record.assert_called_once_with(_sentinel.ud_response)
    verify_record.assert_called_once_with(_sentinel.ud_record)


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
