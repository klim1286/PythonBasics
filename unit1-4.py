n = int(input('Введите целое положительное число: '))
n_max = 0
while n > 0:
    temp = n % 10
    if temp > n_max:
        n_max = temp
    n = n // 10
print(f'Максимум: {n_max}')
