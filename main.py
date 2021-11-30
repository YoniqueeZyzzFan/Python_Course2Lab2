import argparse
import json
from json import JSONEncoder
from tqdm import tqdm
from package.Validator import validation_dict
from package.bucket_sort import bucket_sort as bucket_sort


def rename(dict_to_change: dict) -> dict:
    """
    Rename - фукция, которые переименовывает ключи у словаря
    dict_to_change - словарь, в котором нужно изменить ключи
    return - Возвращает нужный словарь
    """
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


def sorting(path_to_sort: str, path_to_save: str) -> None:
    """
    Sorting - фунцкия сортировка по сегментам (bucket_sort)

    path_to_sort - Путь к данным, которые надо отсортировать
    path_to_save - Путь, куда надо сохранить отсортированные данные
    """
    dict_to_sort = [{}]
    with open(path_to_sort, encoding='utf-8') as file:
        data = json.load(file)
    with tqdm(len(data), desc="Создание словаря с ключами для сортировки") as progressbar:
        for j in data:
            dict_to_sort.append([float(j['height']), j])
            progressbar.update(1)
    sorted_list = bucket_sort(dict_to_sort)
    to_save = []
    for i in sorted_list:
        to_save.append(i.__dict__)
    with tqdm(1, desc="Сериализация данных в JSON и запись в файл") as progressbar:
        with open(path_to_save, encoding='utf-8', mode='w') as file:
            json.dump(to_save, file)
        progressbar.update(1)
    with open(path_to_save, mode='r') as file:
        data = json.load(file)
    load = []
    for i in data:
        load.append(rename(i))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sorting_valid")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-valid', '--validation', help='Запускает валидацию данных в файле')
    group.add_argument('-sort', '--sorting', help='Запускает сортировку данных в файле')
    group.add_argument('-vs', '--validsorting',
                       help='Запускает валидацию данных и последующую их сортировку, если хотите использовать эту функцию, '
                            'то введите еще один аргумент, который будет указывать путь сохранения отсортированных данных')

    parser.add_argument(
        "-input",
        type=str,
        help="Это обязательный строковый позиционный аргумент, который указывает, с какого файла будут считаны данные",
        dest="file_input",
        required=True)
    parser.add_argument(
        "-output",
        type=str,
        help="Это необязательный позиционный аргумент, который указывает, куда будут сохранены отсортированные/валидированные/валидные отсортированные данные",
        dest="file_output",
        required=True)
    args = parser.parse_args()
    dict_to_sort = {}
    if args.validation is not None:
        validation_dict(args.file_input, args.file_output)
    if args.sorting is not None:
        sorting(args.file_input, args.file_output)
    if args.validsorting is not None:
        validation_dict(args.file_input, args.file_output)
        sorting(args.file_output, args.file_output)
        print('____________________________\n')
        print('Unserialize test')
        with open (args.file_output) as file:
            data = json.load(file)
        for i in range(len(data)):
            data[i] = rename(data[i])
        print(data)


