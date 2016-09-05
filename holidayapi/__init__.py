import json
import requests

class v1:
    key = None

    def __init__(self, key):
        self.key = key

    def holidays(self, parameters):
        url = 'https://holidayapi.com/v1/holidays?'

        if parameters.has_key('key') is False:
            parameters['key'] = self.key

        response = requests.get(url, params=parameters);
        data     = json.loads(response.text)

        if response.status_code != 200:
            if data.has_key('error') is False:
                data['error'] = 'Unknown error.'

        return data

