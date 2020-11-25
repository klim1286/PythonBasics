with open('file-1.txt', 'w', encoding='utf-8') as file:
    text = input('Ведите данные: ')
    while text != '':
        file.writelines(text + '\n')
        text = input('Ведите данные: ')
