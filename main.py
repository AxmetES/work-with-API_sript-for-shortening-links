import requests

params_lnd = {'nTqu': '', 'lang': 'en'}
params_rus = {'nTqm': '', 'lang': 'ru'}
url_lnd = 'https://wttr.in/london'
url_svo = 'https://wttr.in/SVO'
url_chr = 'https://wttr.in/Cherepovets'


def get_response(url, params):
    response = requests.get(url, params=params)
    print(response.text)


get_response(url_lnd, params_lnd)
get_response(url_svo, params_rus)
get_response(url_chr, params_rus)
