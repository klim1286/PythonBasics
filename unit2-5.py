my_list = [7, 5, 3, 3, 2]
while True:
    user = input('Введите показатель рейтинга. Для завершения ввода введите "q". ')
    if user == 'q':
        break
    else:
        user = int(user)
        list_count = my_list.count(user)
        if list_count > 0:
            my_list.insert(my_list.index(user)+list_count,user)
            print(my_list)
        else:
            n = 0
            i = user
            while n == 0:
                i -= 1
                n = my_list.count(i)
                if n > 0:
                    my_list.insert(my_list.index(i), user)
                    print(my_list)
                elif i == 0:
                    while n == 0:
                        i += 1
                        n = my_list.count(i)
                        if n > 0:
                            my_list.insert(my_list.index(i) + +n + 1, user)
                            print(my_list)
