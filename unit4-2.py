from random import randint as rnd
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_list = [gen + rnd(0, 100) for gen in range(rnd(5, 15))]
gen = [el for el in my_list[1:] if el > my_list[my_list.index(el) - 1]]
print(my_list)
print(gen)
