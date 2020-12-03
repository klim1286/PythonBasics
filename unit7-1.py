class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        i, j = 0, 0
        sumMatrix, en = [], []
        if len(self.matrix) == len(other.matrix):
            try:
                for el in self.matrix:
                    if len(el) == len(other.matrix[i]):
                        for zn in el:
                            en.append(zn + other.matrix[i][j])
                            j += 1
                        i += 1
                        j = 0
                        sumMatrix.append(en)
                        en = []
                    else:
                        return 'Ошибка! Матрицы разных размеров!'
                return Matrix(sumMatrix)
            except IndexError:
                return 'Ошибка! Матрицы разных размеров!'
        else:
            return 'Ошибка! Матрицы разных размеров!'

    def __str__(self):
        txt = ''
        for el in self.matrix:
            for zn in el:
                txt += f'{str(zn)}   '
            txt += '\n\n'
        return txt


matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5], [2, 4], [-1, 64]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
