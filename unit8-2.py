class ZeroErr(Exception):
    def __init__(self, text):
        self.text = text


a = input("Введите делимое: ")
b = input("Введите делитель: ")

try:
    a = int(a)
    b = int(b)
    if b == 0:
        raise ZeroErr("Нельзя делить на 0")
    else:
        print(a / b)
except (ValueError, ZeroErr) as txt:
    print(txt)
