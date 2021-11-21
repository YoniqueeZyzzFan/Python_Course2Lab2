import json
import Validator
from tqdm import tqdm
import argparse


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


def sort_list(list_to_sort: list) -> list:
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    return list_to_sort


def bucket_sort(dict_to_sort: dict) -> list:
    list_keys = list(dict_to_sort)
    x = max(list_keys)
    splitter = float(x) / float(len(list_keys))
    bucket_list = []
    for i in range(len(list_keys)):
        bucket_list.append([])
    with tqdm(len(list_keys), desc="Разбиение на сегменты для сортировки") as progressbar:
        for i in range(len(list_keys)):
            j = int(list_keys[i] / splitter)
            if j != len(list_keys):
                bucket_list[j].append(list_keys[i])
            else:
                bucket_list[len(list_keys) - 1].append(list_keys[i])
        progressbar.update(1)
    sorted_keys = []
    with tqdm(bucket_list, desc="Сортировка сегментов") as progressbar:
        for i in range(len(bucket_list)):
            sorted_keys = sorted_keys + (sort_list(bucket_list[i]))
            progressbar.update(1)
    result_list = []
    for key in sorted_keys:
        result_list.append(Validator.Validator(dict_to_sort[key]))
    return result_list


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
