import requests
import argparse
from urllib.parse import urlsplit
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
headers = {"Authorization": f"Bearer {TOKEN}"}

params = {"unit": "day", "units": -1}

url_shorten = 'https://api-ssl.bitly.com/v4/shorten'

parser = argparse.ArgumentParser(description='bitly shorted link')
parser.add_argument('long_link', type=str)
args = parser.parse_args()


def get_short(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as error:
        print(f'error \n{error}')


def get_total_clicks(url, headers, params):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        json_data = response.json()
        return json_data
    except requests.exceptions.HTTPError as error:
        print(f'error \n{error}')


def get__link(data):
    if 'total_clicks' in data:
        get__link = data['total_clicks']
        return get__link
    else:
        get__link = data['link']
        return get__link


def check_link(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(f'link error: \n{error}')
        exit()


def url_split(url):
    base_url = "{0.netloc}{0.path}".format(urlsplit(url))
    return base_url


def main():
    check_link(args.long_link)

    if 'bit.ly' in args.long_link:
        bitlink = args.long_link
        cut_link = url_split(bitlink)
        url_clicks = f'https://api-ssl.bitly.com/v4/bitlinks/{cut_link}/clicks/summary'
        json_summ_clicks = get_total_clicks(url_clicks, headers, params)
        print('')
        print(f'количество кликов по ссылке: {get__link(json_summ_clicks)}')
    else:
        body = {"long_url": args.long_link}
        short_json = get_short(url_shorten, headers, body)
        bitlink = get__link(short_json)
        print(f'Битлинк: {bitlink}')


if __name__ == '__main__':
    main()
