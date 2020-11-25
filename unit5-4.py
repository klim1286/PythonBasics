from googletrans import Translator

err_i = 0
translator = Translator()


def tran(word):
    return translator.translate(word, dest='ru', src='auto').text


while True:
    try:
        with open('text_4.txt', 'r', encoding='utf-8') as input_file:
            with open('text_4_translate.txt', 'w', encoding='utf-8') as output_file:
                for out in input_file:
                    z = str(out.split()[0])
                    back = ''.join(out.split()[1: -1])
                    output_file.writelines(f'{tran(z)} {back} \n')
        if err_i == 0:
            print('Ошибок в работе модуля "googletrans" не было')
        else:
            print(f'Всего ошибок в работе модуля "googletrans": {err_i}')
        break
    except AttributeError:
        err_i += 1
        print(f'Ошибка в работе модуля "googletrans" № {err_i}')
        if err_i <= 100:
            continue
        else:
            print('Слишком много ошибок, необходимо запустить программу еще раз')
            break
