def person(**kwargs):
    string = ' '.join(kwargs.values())
    print(string)


name_in = input('Введите имя: ')
lname_in = input('Введите фимилию: ')
byear_in = input('Введите год рождения: ')
city_in = input('Введите город проживания: ')
email_in = input('Введите email: ')
phone_in = input('Введите телефон: ')

person(name=name_in, lname=lname_in, byear=byear_in, city=city_in, email=email_in, phone=phone_in)
