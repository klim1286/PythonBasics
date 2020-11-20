from functools import reduce


def my_prod(a1, a2):
    return a1 * a2


print(reduce(my_prod, [el for el in range(100, 1001) if el % 2 == 0]))
