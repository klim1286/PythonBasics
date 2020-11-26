try:
    with open('file-1.txt', 'r', encoding='utf-8') as file:
        i, z = 0, 0
        for ln in file:
            z += len(ln.split())
            i += 1
    print(f'Всего строк: {i}, Всего слов: {z}')
except FileNotFoundError:
    print('Error! File Not Found!')
except PermissionError:
    print('Error! Permission denied!')
