import json
import requests


def get_esv_text(passage,api_config):

    url = "%s/passage/text/" % api_config.api_url

    params = {
        'q': passage,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % api_config.api_key
    }

    

    response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print(response.text)
        raise Exception(response.text)
    else:
        passages = response.json()['passages']

    return passages[0].strip() if passages else 'Error: Passage not found'
