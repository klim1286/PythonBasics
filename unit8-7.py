class OperationComplexNum:
    def __init__(self, numb, compl):
        self.numb = numb
        self.compl = compl

    def __str__(self):
        return f'{complex(self.numb, self.compl)}'

    def __add__(self, other):
        return OperationComplexNum(self.numb + other.numb, self.compl + other.compl)

    def __mul__(self, other):
        x = (self.numb * other.numb) + (self.compl * other.compl * -1)
        y = (self.numb * other.compl) + (self.compl * other.numb)
        return OperationComplexNum(x, y)


numb1 = OperationComplexNum(3, 1)
numb2 = OperationComplexNum(2, -3)
print(numb1 + numb2)
print(numb1 * numb2)
