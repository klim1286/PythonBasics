from sys import argv

try:
    name, job, rate, premium = argv
    print(f' Зарплата составляет: {int(job) * int(rate) + int(premium)}')
except ValueError:
    print('Некорректный ввод')
