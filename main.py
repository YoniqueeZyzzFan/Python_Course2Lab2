import re
import json
import os
from tqdm import tqdm
import argparse


class Human:
    """
       class Human - принимает в себя словарь данных о каком либо пользователя, и с помощью его методов, можно проверить их корекктность
       Attributes:
           email: str - хранит электронную почту пользователя
           height: str - хранит рост пользователя
           snils: str - хранит номер снилса пользователя
           passport_series: str - хранит серию паспорта пользователя
           university: str - хранит вуз пользователя
           age: str - хранит возраст пользователя
           political_view: str - хранит политические взгляды пользователя
           worldview: str - хранит взгляд на мир пользователя
           address: str - хранит адрес проживания пользователя
           info_worldview: list - хранит список, со взглядами на мир
           info_political: list - хранит список, с полит. взглядами
           info_univer: list - хранит список, невалидных университетов
       """

    def __init__(self, d):
        """
        __init__ - служит для записи данных пользователя в различные поля
        :param d: - передает словарь данных о человеке
        """
        self.__data = d
        self.__height = float(d['height'])

    @property
    def height(self) -> float:
        '''
        height - метод, который вернет рост человека
        :return: object
        '''
        return self.__height


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
    for i in range(len(list_keys)):
        j = int(list_keys[i] / splitter)
        if j != len(list_keys):
            bucket_list[j].append(list_keys[i])
        else:
            bucket_list[len(list_keys) - 1].append(list_keys[i])
    sorted_keys = []


if __name__ == "__main__":
    path = "G:\\PythonLabs\\PrikladnoePrLab3\\Unsorted.json"
    path2 = "G:\\PythonLabs\\PrikladnoePrLab3\\Sorted.json"
    dict_to_sort = {}
    with open(path, encoding='utf-8') as file:
        data = json.load(file)
    for j in data:
        dict_to_sort[float(j['height'])] = j
    sorted_list = bucket_sort(dict_to_sort)
    with open(path2, encoding='utf-8', mode='w') as file:
        json.dump(sorted_list, file)
