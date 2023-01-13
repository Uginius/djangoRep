import json
import os
from DjangoRep.settings import *
from rep3.models import Category


def load_json(json_filename):
    with open(json_filename, 'r', encoding='utf8') as read_file:
        result = json.load(read_file)
    return result


def get_json_data(folder):
    loaded_data = {}
    json_files = sorted(os.listdir(folder))
    for name in json_files:
        file_data = load_json(f'{folder}/{name}')
        continue


if __name__ == '__main__':
    # get_json_data('rep3/2022-December')
    src = load_json('rep3/src_xls_data.json')
    for shop, shop_data in src.items():
        shop_cats = list(shop_data)
        print(shop_cats)
        break
    pass
