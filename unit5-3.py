with open('text_3.txt', 'r', encoding='utf-8') as file:
    z = [el.split()[0] for el in file if float(el.split()[1]) < 20000]
    file.seek(0)
    mean = [float(el2.split()[1]) for el2 in file]
    mean = sum(mean) / len(mean)
print(' '.join(z))
print(f'Средний заработок сотрудников: {mean}')
