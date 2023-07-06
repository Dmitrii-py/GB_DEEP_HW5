# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии
# (решение задачи "не в одну строку" есть на 4 семинаре(5 задача))

name_list = ['Ivan', 'Piter', 'Andrew']
salary_list = [1000, 2000, 3000]
extra_list = ['10.25%', '15%', '20%']

result = {name: salary * extra for name, salary, extra
          in zip(name_list, salary_list,
                 list(map(lambda x: float(x[:-1]) / 100, extra_list)))}
print(result)
