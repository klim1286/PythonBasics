def srt_to_int(*args):
    sum_int = 0
    for i in args:
        prom = ''.join([el for el in i if 48 <= ord(el) <= 57])
        if prom != '':
            sum_int += int(prom)
    return sum_int


sum1, sum2, sum3 = 0, 0, 0
slov = {}
with open('text_6.txt', 'r', encoding='utf-8') as file:
    for txt in file:
        sp = txt.split()
        sum1 = srt_to_int(sp[1], sp[2], sp[3])
        slov.update({sp[0][:-1]: sum1})
print(slov)
