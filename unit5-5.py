with open('text_5.txt', 'w+', encoding='utf-8') as file:
    file.writelines('2376 232 8374 26 234')
    file.seek(0)
    print(sum(map(int, file.readline().split())))
