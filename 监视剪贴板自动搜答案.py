from time import sleep

import pyperclip
import requests
from urllib import parse
import re


def search(data):
    data = parse.quote(data)
    url = 'http://api.xmlm8.com/'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post(url, data='w=' + data, headers=headers)
    try:
        key = re.search('(答案：.+)</span>', r.text).groups()
        print(key[0])
    except AttributeError:
        print('未找到答案！')


if __name__ == '__main__':
    sleep(2)
    data = pyperclip.paste()
    search(data)
    while 1:
        sleep(0.2)
        new_data = pyperclip.paste()
        if data != new_data:
            search(new_data)
            new_data, data = data, new_data
        else:
            pass
