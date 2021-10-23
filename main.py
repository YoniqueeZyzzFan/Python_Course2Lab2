# Lab 2 Variant 67

import re
import json
import os
from tqdm import tqdm
import argparse


class File:
    """
    Объект класса File нужен, для хранения данных из файла,
    которые должны подвергнуться валидации.
    Attributes:
        __data - хранит в себе данные, считанные с файла
    """
    __data: object

    def __init__(self, f: str):
        """
        __init__ - инициалузирует экземпляр класса данных с файла
        :param f: Показывает путь к файлу с данными, которые необходиммо считать
        """
        try:
            if os.path.getsize(f) > 0:
                self.__data = json.load(open(f, encoding='windows-1251'))
        except OSError:
            print("В файле хранится неверный формат данных или файла по данному пути не существует")

    @property
    def data(self):
        '''
        get_data - метод, который вернет данные содержащиеся в поле data
        :return: object
        '''
        return self.__data


class Validator:
    """
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
    """
    __email: str
    __height: str
    __snils: str
    __passport_series: str
    __university: str
    __age: str
    __political_views: str
    __worldview: str
    __address: str

    def __init__(self, d: dict):
        """
        __init__ - служит для записи данных пользователя в различные поля, для проведенеия валидации
        :param d: - передает данные, которые нужно записать в валидатор
        """
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
        if re.match(r"[\w.-]+[\w]+@[\w]+[?.\w]\w{2,4}[.]\w+$", self.__email) is None:
            return 'email'
        if re.match(r"[\d]+?[.]\d+", str(self.__height)) is None or float(self.__height) <= 0 or float(
                self.__height) >= 230:
            return 'height'
        if re.match(r"[\d]{11}", self.__snils) is None:
            return 'snils'
        if re.match(r"^[\d]{2}? [\d]{2}", self.__passport_series) is None:
            return 'passport'
        if re.match(r"^[\D]+", self.__university) is None:
            return 'university'
        if re.match(r"^\d+", str(self.__age)) is None or 0 >= int(self.__age) >= 120:
            return 'age'
        if re.match(r"^[\D]+$", self.__worldview) is None:
            return 'worldview'
        if re.match(r"(^ул\.\s[\w .-]+\d+)", self.__address) is None:
            return 'address'
        if re.match(r"^\D+$", self.__political_views) is None:
            return 'political'
        return "True"


parser = argparse.ArgumentParser(description="main")
parser.add_argument("-input", type=str,
                    help="Это обязательный строковый позиционный аргумент, который указывает, с какого файла будут считаны данные",
                    dest="file_input")
parser.add_argument("-output", type=str,
                    help="Это необязательный позиционный аргумент, который указывает, куда будут сохранены валидные данные",
                    dest="file_output")
args = parser.parse_args()
file = File(args.file_input)
output = open(args.file_output, 'w')

dict_err = {"email": 0,
            "height": 0,
            "snils": 0,
            "passport": 0,
            "univer": 0,
            "age": 0,
            "worldview": 0,
            "address": 0,
            "political": 0,
            "True": 0}
counter = 0
for i in file.data:
    counter += 1
counter_false = 0
with tqdm(total=100) as progressbar:
    for i in file.data:
        f = Validator(i)
        dict_err[f.validation()] += 1
        if f.validation() == "True":
            output.write("email: " + i["email"] + "\n" + "height:" + str(i["height"]) + "\n" +
                         "snils: " + str(i["snils"]) + "\n" + "passport_series:" + str(i["passport_series"]) + "\n" +
                         "university: " + i["university"] + "\n" + "age: " + str(i["age"]) + "\n" +
                         "political_views: " + i["political_views"] + "\n" + "worldview: " + i["worldview"] + "\n"
                         + "address: " + i["address"] + "\n" + "__________________________________________\n")
        else:
            counter_false += 1
        progressbar.update(100 / counter)

print("Количество ошибок из-за опредленных полей: \nВсего пользователей: " + str(
    counter) + "\nЧисло валидных записей - " + str(counter - counter_false) + "\nЧисло невалидных записей - " + str(
    counter_false))
for i in dict_err:
    print(i + ": " + str(dict_err[i]))
output.close()
