import argparse
import requests


def main():
    args = set_up_arguments()
    term = args.term
    request = 'http://localhost:5127?term={}'.format(term)
    json_result = requests.get(request).json()
    print_records(json_result)


def set_up_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'term',
        help='the search time to lookup on Urban Dictionary'
    )

    return parser.parse_args()


def print_records(record):
    print('Term: {}'.format(record['word']))
    print('Definition: {}'.format(record['definition']))
    print('Example: {}'.format(record['example']))


if __name__ == '__main__':
    main()
