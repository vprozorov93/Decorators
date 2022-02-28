import logging
import os
import requests
import re


def decorator(path):
    def _decorator(function):
        def func_of_decorator(*args):
            logging.basicConfig(
                level=logging.INFO,
                filemode='a',
                filename=os.path.join(path, 'log_file.log'),
                format='[%(asctime)s] %(levelname)s: %(message)s'
            )
            logging.info(f'Executing function "{function.__name__}" with arguments: {args}')
            result = function(*args)
            logging.info(f'Function "{function.__name__}" return value {result}')
            return result

        return func_of_decorator

    return _decorator


@decorator('.')
def get_my_ip(url):
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    ip_address_v2 = re.search(r'(\d+\.\d+\.\d+\.\d+)(</span>)', text).group(1)
    return ip_address_v2


if __name__ == '__main__':
    decorator(get_my_ip('https://2ip.ru'))
