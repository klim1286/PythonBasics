def int_func(phrase):
    text_end = []
    n = 0
    """Перебор слов в фразе"""
    for element in phrase.split():
        """Перебор букв в слове"""
        for i in element:
            """
            Если буква не соответсвует фильтру слово отбрасываем,
            счетчик 'n' обнуляем.
            """
            if ord(i) < 97 or ord(i) > 122:
                n = 0
                break
            else:
                n += 1
        """
        Если все буквы прошли фильтр, слово добавляем в список,
        счетчик 'n' обнуляем.
        """
        if len(element) == n:
            text_end.append(element.title())
            n = 0
    """Возвращаем отфильтрованную фразу разбивая пробелом"""
    return ' '.join(text_end)


text = input('Введите текст: ')
print(int_func(text))
