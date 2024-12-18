def get_matrix (n, m, value) :
    matrix = []
    if value == 0 :
        return matrix
    else :
        for i in range(n) :
            x = []
            for j in range(m) :
                x.append(value)
            matrix.append(x)
    return matrix


a = int(input('Введите число строк: '))
b = int(input('Введите число столбцов: '))
c = int(input('Введите значение: '))
result = get_matrix(a, b, c)

for i in result :
    print(i)