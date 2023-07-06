# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')

def separate_path_info(path: str) -> tuple[str]:
    *absolute, file = path.split('/')
    print(file)
    return '/'.join(absolute), *file.split('.')


print(separate_path_info('c:/Users/Vladislav/Desktop/deep_to_python/test.txt'))
