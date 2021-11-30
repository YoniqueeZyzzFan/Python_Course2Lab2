from package.Validator import *
from tqdm import tqdm


def sort_list(list_to_sort: list) -> list:
    '''
    sort_list - функция, которая сортирует список
    list_to_sort - список, которые необходимо отсортировать
    return - list - Возвращает отсортированный список
    '''
    for i in range(len(list_to_sort)):
        for j in range(i + 1, len(list_to_sort)):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
    return list_to_sort


def bucket_sort(dict_to_sort: list) -> list:
    '''
    bucket_sort - функция сортировки по сегментам, алгоритмическая сложность О(n)
    dict_to_sort - словарь с ключами, по которым будет производится сортировка
    return - list - возвращает список отсортированных словарей
    '''
    all_keys = []
    for i in range(1, len(dict_to_sort)):
        all_keys.append(dict_to_sort[i][0])
    list_keys = list(all_keys)
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
            sorted_keys = sorted_keys + sort_list(bucket_list[i])
            progressbar.update(1)
    result_list = []
    for key in sorted_keys:
            result_list.append({key, Validator(dict_to_sort[key])})
    return result_list
