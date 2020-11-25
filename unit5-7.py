import json


i = 0
firm_profit = {}
dict_averange = {}
lt_all = []
profit = 0
with open('text_7.txt', 'r', encoding='utf8') as file:
    for line in file:
        check = int(line.split()[2])
        pay = int(line.split()[3])
        if check >= pay:
            i += 1
            profit = (profit + check - pay)
            average_profit = profit / i
            firm_profit.update({line.split()[0]: check - pay})
        else:
            firm_profit.update({line.split()[0]: check - pay})

dict_averange.update({'average_profit': average_profit})
lt_all.append(firm_profit)
lt_all.append(dict_averange)

with open('text_7j.json', 'w', encoding='utf-8') as file:
    file.writelines(json.dumps(lt_all,
                               sort_keys=False,
                               indent=4,
                               ensure_ascii=False,
                               separators=(',', ': '))
                    )
