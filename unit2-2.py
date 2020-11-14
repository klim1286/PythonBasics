elements = input('Введите элементы списка через пробел: ').split()
i = 0
for el in range(len(elements) // 2):
    el1 = elements[i]
    el2 = elements[i + 1]
    elements[i] = el2
    elements[i + 1] = el1
    i += 2
print(elements)
