# Создайте функцию генератор чисел Фибоначчи

from typing import Iterator


def fib_gen(n: int) -> Iterator:
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

print(list(fib_gen(10)))
