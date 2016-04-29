import argparse
import requests

from udplugin.errors.InvalidRecordError import InvalidRecordError
from udplugin.errors.InvalidSearchError import InvalidSearchError
from udplugin.errors.InvalidStatusError import InvalidStatusError
from udplugin.errors.UDError import UDError
from udplugin.UDRequestHandler import UDRequestHandler


def main():
    args = set_up_arguments()
    term = args.term
    request_handler = UDRequestHandler(requests)
    status_code, word, definition, example = request_handler.search(term)
    print_records((word, definition, example))


def set_up_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'term',
        help='the search time to lookup on Urban Dictionary'
    )

    return parser.parse_args()


def print_records(record):
    word, definition, example = record
    print('Term: {}'.format(word))
    print('Definition: {}'.format(definition))
    print('Example: {}'.format(example))

if __name__ == '__main__':
    main()
