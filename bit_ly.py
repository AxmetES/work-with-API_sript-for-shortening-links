import requests
import argparse
from urllib.parse import urlsplit
import os

from dotenv import load_dotenv
from urllib3.exceptions import HTTPError

PARAMS = {"unit": "day", "units": -1}
URL_SHORT = 'https://api-ssl.bitly.com/v4/shorten'


def get_parser():
    parser = argparse.ArgumentParser(description='bitly shorted link')
    parser.add_argument('long_link', type=str)
    args = parser.parse_args()
    return args


def get_short(url, headers, data):
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    json_data = response.json()
    return json_data


def get_total_clicks(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    json_data = response.json()
    return json_data


def get__link(data):
    if 'total_clicks' in data:
        link = data['total_clicks']
        return link
    else:
        link = data['link']
        return link


def check_link(url):
    response = requests.get(url)
    response.raise_for_status()


def get_split_url(url):
    base_url = "{0.netloc}{0.path}".format(urlsplit(url))
    return base_url


def main():
    args = get_parser()
    get_parser()
    load_dotenv(verbose=True)
    token_bitly = os.getenv('TOKEN_BITLY')
    headers = {"Authorization": f"Bearer {token_bitly}"}

    try:
        check_link(args.long_link)

        if 'bit.ly' in args.long_link:
            bitlink = args.long_link
            cropped_link = get_split_url(bitlink)
            total_clicks_url = f'https://api-ssl.bitly.com/v4/bitlinks/{cropped_link}/clicks/summary'
            json_summ_clicks = get_total_clicks(total_clicks_url, headers, PARAMS)
            print('')
            print(f'количество кликов по ссылке: {get__link(json_summ_clicks)}')
        else:
            body = {"long_url": args.long_link}
            json_short_link = get_short(URL_SHORT, headers, body)
            bitlink = get__link(json_short_link)
            print(f'Битлинк: {bitlink}')
    except HTTPError as error:
        print(f'{error}')
        exit()


if __name__ == '__main__':
    main()
