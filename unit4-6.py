from itertools import count, cycle


def a_generate(start, end):
    a = []
    for el in count(start):
        if el > end:
            return a
        a.append(el)


def b_generate(other_list):
    b = []
    i = 0
    for el in cycle(other_list):
        if i > 15:
            return b
        i += 1
        b.append(el)


my_list = ["Name", "Last name", 89001234567, False, True]
print(a_generate(3, 10), b_generate(my_list))
