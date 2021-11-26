import argparse
import json
from tqdm import tqdm
from package.Validator import Validator
from package.bucket_sort import bucket_sort as bucket_sort


def rename(dict_to_change: dict) -> dict:
    new_dict = {}
    new_dict['email'] = dict_to_change['_Validator__email']
    new_dict['height'] = dict_to_change['_Validator__height']
    new_dict['snils'] = dict_to_change['_Validator__snils']
    new_dict['passport_series'] = dict_to_change['_Validator__passport_series']
    new_dict['university'] = dict_to_change['_Validator__university']
    new_dict['age'] = dict_to_change['_Validator__age']
    new_dict['political_views'] = dict_to_change['_Validator__political_views']
    new_dict['worldview'] = dict_to_change['_Validator__worldview']
    new_dict['address'] = dict_to_change['_Validator__address']
    return new_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sorting_valid")
    parser.add_argument(
        "-input",
        type=str,
        help="Это обязательный строковый позиционный аргумент, который указывает, с какого файла будут считаны данные",
        dest="file_input")
    parser.add_argument(
        "-output",
        type=str,
        help="Это необязательный позиционный аргумент, который указывает, куда будут сохранены отсортированные данные",
        dest="file_output")
    args = parser.parse_args()
    dict_to_sort = {}
    with open(args.file_input, encoding='utf-8') as file:
        data = json.load(file)
    with tqdm(len(data), desc="Создание словаря с ключами для сортировки") as progressbar:
        for j in data:
            dict_to_sort[float(j['height'])] = j
            progressbar.update(1)
    sorted_list = bucket_sort(dict_to_sort)
    to_save = []
    for i in sorted_list:
        to_save.append(i.__dict__)
    with open(args.file_output, encoding='utf-8', mode='w') as file:
        json.dump(to_save, file)
    with open(args.file_output, mode='r') as file:
        data = json.load(file)
    load = []
    for i in data:
        load.append(rename(i))
