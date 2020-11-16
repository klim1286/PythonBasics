my_list = input('Введите предложение: ').split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[:10])
