from package.Validator import *
from tqdm import tqdm


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
        result_list.append(Validator(dict_to_sort[key]))
    return result_list
