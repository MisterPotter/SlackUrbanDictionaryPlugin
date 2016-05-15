import requests

from udplugin.errors.InvalidRecordError import InvalidRecordError
from udplugin.errors.InvalidSearchError import InvalidSearchError
from udplugin.errors.InvalidStatusError import InvalidStatusError
from udplugin.errors.UDError import UDError


class UDRequest:

    def __init__(self):
        self._base_url = 'http://api.urbandictionary.com/v0/define?term={}'

    def __repr__(self):
        return 'UDRequestHandler()'

    def __call__(self, term):
        return self.search(term)

    def search(self, term):
        """Uses the requests module to obtain a response and then uses the
           information from the response to create a UDTerm node

        :term type: string
        :term: The term to search Urban Dictionary for

        :rtype: dict
        :return: a dict containing a single response from Urban Dictionary
        """
        response = requests.get(self._base_url.format(term))
        try:
            record = self.response_to_record(response)
            self.verify_record(record)

            return record
        except UDError as e:
            # TODO: Doc propagate error up?
            print(e)

    @staticmethod
    def response_to_record(response):
        """Translates an HTTP reponse to a UD Record"""
        json_data = response.json()
        all_definitions = json_data['list']
        status_code = response.status_code
        word, definition, example = (None, None, None)

        if json_data.get('result_type', 'no_results') != 'no_results':
            first_definition = all_definitions[0]
            word = first_definition.get('word', None)
            definition = first_definition.get('definition', None)
            example = first_definition.get('example', None)

        return (
            status_code,
            word,
            definition,
            example
        )

    @staticmethod
    def verify_record(record):
        """Verifies a UDRecord and throws an error if there are any
           discreptencies.

        :record type: dict
        :record: a dict with the attributes, status_code, word, definitionm
            and example
        """
        try:
            status_code, word, definition, example = record
        except ValueError:
            raise InvalidRecordError()

        if status_code != 200:
            raise InvalidStatusError(status_code)

        if not word:
            raise InvalidSearchError()
