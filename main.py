# Lab 2 Variant 67

import re
import json
import time
import os
from tqdm import tqdm


class File:
    '''
    Объект класса File нужен, для хранения данных из файла,
    которые должны подвергнуться валидации.
    Attributes:
        __data - хранит в себе данные, считанные с файла
    '''
    __data: object

    def __init__(self, f: str):
        '''
        __init__ - инициалузирует экземпляр класса данных с файла
        :param f: Показывает путь к файлу с данными, которые необходиммо считать
        '''
        try:
            if os.path.getsize(f) > 0:
                self.__data = json.load(open(f, encoding='windows-1251'))
        except OSError:
            print("В файле хранится неверный формат данных или файла по данному пути не существует")

    def get_data(self):
        '''
        get_data - метод, который вернет данные содержащиеся в поле data
        :return:
        '''
        return self.__data


class Validator:
    '''
    class Validator - принимает в себя данные о каком либо пользователя, и с помощью его методов, можно проверить их корекктность
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
    '''
    __email: str
    __height: str
    __snils: str
    __passport_series: str
    __university: str
    __age: str
    __political_views: str
    __worldview: str
    __address: str

    def __init__(self, d: object):
        '''
        __init__ - служит для записи данных пользователя в различные поля, для проведенеия валидации
        :param d: - передает данные, которые нужно записать в валидатор
        '''
        self.__email = d['email']
        self.__height = d['height']
        self.__snils = d['snils']
        self.__passport_series = d['passport_series']
        self.__university = d['university']
        self.__age = d['age']
        self.__political_views = d['political_views']
        self.__worldview = d['worldview']
        self.__address = d['address']

    def validation(self):
        if re.findall(r"[\w\.-]+[\w]+@[\w]+[?\.\w]\w{2,4}[.]\w+$", self.__email) is None:
            raise "email"
        if re.findall(r"[\d]+?[\.]\d+", self.__height) is None and float(self.__height) <= 0 and float(
                self.__height) >= 230:
            raise "height"
        if re.findall(r"[\d]{11}", self.__snils) is None:
            raise "snils"
        if re.findall(r"^[\d]{2}? [\d]+", self.__passport_series) is None and len(
                re.findall(r"^[\d]{2}? [\d]+", self.__passport_series)) != len(self.__passport_series):
            raise "passport_series"
        if re.findall(r"^[\D]+", self.__university) is None:
            raise "university"
        if re.findall(r"^[\d]{3}$", self.__age) is None and 0 >= int(self.__age) >= 120:
            raise "age"
        if re.findall(r"^[\D]+$", self.__worldview) is None:
            raise "worldview"
        if re.findall(r"^(?:ул. \w+)\ (\w|\ )(\W+|\w+)\d+$", self.__address) is None:
            raise "address"
        if re.findall(r"^\D+$", self.__political_views) is None:
            raise "political_views"

        path = '67.txt'
        path_to_save = '69.txt'
        data = File(path)
        err_email = 0
        err_height = 0
        err_snils = 0
        err_passport = 0
        err_univer = 0
        err_age = 0
        err_worldview = 0
        err_address = 0
        err_political = 0


