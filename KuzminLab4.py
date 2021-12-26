# Variant - 4

# from multiprocessing import Pool
import datetime
from tqdm import tqdm, trange
import concurrent.futures
from math import sqrt
import argparse


def doubled(x: float) -> float:
    return x * x


def solution_without(first: float, second: float) -> float:
    hyp = sqrt(doubled(first) + doubled(second))
    return hyp


def test_time_without_threads(first: float, second: float, count: int) -> None:
    start_time = datetime.datetime.now()
    print('_____Without threads_____')
    hyp = 0
    with tqdm(count, desc='Считаем гипотенузу..') as progressbar:
        for i in range(count):
            hyp = solution_without(first, second)
            i += 1
            progressbar.update(1 / count)
    print(hyp)
    result = datetime.datetime.now() - start_time
    print(result)


def solution_with(first: float, second: float) -> float:
    hyp = 0
    with concurrent.futures.ThreadPoolExecutor() as thr:
        a = thr.submit(doubled, first)
        b = thr.submit(doubled, second)
        hyp = sqrt(a.result() + b.result())
    return hyp


def test_time_with_threads(first: float, second: float, count: int) -> None:
    print('_____With threads_____')
    start_time = datetime.datetime.now()
    hyp = 0
    #with tqdm(count, desc='Считаем гипотенузу..') as progressbar:
    for i in trange(count):
        hyp = solution_with(first, second)
        i += 1
    #        progressbar.update(1 / count)
    print(hyp)
    result = datetime.datetime.now() - start_time
    print(result)


# def solution_with_multiprocsessing(first: float, second: float) -> None:
#    with Pool(5) as p:
#        print(p.map(doubled, [first, second]))


# def test_time_with_multiprocessing(first: float, second: float, count: int) -> None:
#    print('_____With multiprocessing_____')
#    start_time = datetime.datetime.now()
#    with tqdm(count, desc='Считаем гипотенузу..') as progressbar:
#        for i in range(count):
#            solution_with_multiprocsessing(first, second)
#            i += 1
#            progressbar.update(1 / count)
#    result = datetime.datetime.now() - start_time
# 0    print(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sorting_valid")
    parser.add_argument(
        "-first",
        type=float,
        help="Это обязательный строковый позиционный аргумент, который указывает длину первого катета",
        dest="first_length",
        required=True)
    parser.add_argument(
        "-second",
        type=float,
        help="Это необязательный позиционный аргумент, который указывает длину второго катета",
        dest="second_length",
        required=True)
    args = parser.parse_args()
    if (args.first_length <= 0 or args.second_length <= 0):
        print('Длины сторон не могут быть <= 0 :)')
    else:3
        test_time_without_threads(args.first_length, args.second_length, 100000)
        test_time_with_threads(args.first_length, args.second_length, 100000)
        # test_time_with_multiprocessing(args.first_length, args.second_length, 100000)
