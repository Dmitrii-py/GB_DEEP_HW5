# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')
from typing import Tuple, Any


def get_path_file_ext(path: str) -> tuple[str, Any]:
    *abs_patch, file = path.split('/')
    return '/'.join(abs_patch), *file.split('.')


print(get_path_file_ext('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))



# from os import path
# def get_path_file_ext(my_path: str) -> tuple[str]:
#     abs_path = path.abspath(my_path)
#     file_name = path.basename(my_path)
#     file_ext = path.splitext(file_name)[1]
#     return abs_path, file_name, file_ext
#
# print(get_path_file_ext('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))
