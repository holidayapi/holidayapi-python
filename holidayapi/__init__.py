import json
import requests

class v1:
    def __init__(self, key):
        self.key = key

    def holidays(self, parameters):
        url = 'https://holidayapi.com/v1/holidays?'

        if not parameters.get('key'):
            parameters['key'] = self.key
        else:
            assert self.key == parameters['key'], 'keys supplied as an argument & in `parameters` differ. \n Provide at only one place'

        response = requests.get(url, params=parameters);
        data = response.json()

        if not response.ok:
            if not data.get('error'):
                data['error'] = 'Unknown error.'

        return data
