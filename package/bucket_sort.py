from package.Validator import *
from tqdm import tqdm
from tqdm import trange


def sort_list(list_to_sort: list) -> list:
    '''
    sort_list - функция, которая сортирует список
    list_to_sort - список, которые необходимо отсортировать
    return - list - Возвращает отсортированный список
    '''
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i]['height'] > list_to_sort[j]['height']:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    return list_to_sort


def bucket_sort(dict_to_sort: list) -> list:
    '''
    bucket_sort - функция сортировки по сегментам, алгоритмическая сложность О(n)
    dict_to_sort - словарь с ключами, по которым будет производится сортировка
    return - list - возвращает список отсортированных словарей
    '''
    list_keys = []
    for i in range(0, len(dict_to_sort)):
        list_keys.append(float(dict_to_sort[i]['height']))
    x = max(list_keys)
    splitter = float(x) / float(len(list_keys))
    bucket_list = []
    for i in range(len(list_keys)):
        bucket_list.append([])
    print('Разбиение на сегменты для сортировки:')
    for i in trange(len(dict_to_sort)):
        j = int(float(dict_to_sort[i]['height']) / splitter)
        if j != len(dict_to_sort):
            bucket_list[j].append(dict_to_sort[i])
        else:
            bucket_list[len(dict_to_sort) - 1].append(dict_to_sort[i])
    sorted_bucket = []
    print('Сортировка сегментов:')
    for i in trange(len(bucket_list)):
        temp_list = sort_list(bucket_list[i])
        for j in temp_list:
            sorted_bucket.append(Validator(j))
    return sorted_bucket
