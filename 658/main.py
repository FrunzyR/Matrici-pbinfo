def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def compute_sum(lista):
    suma = 0
    for element in lista:
        suma += element
    return suma


def solve(matrix):
    sum_list = []
    for row in matrix:
        sum_list.append(str(compute_sum(row)))
    return " ".join(sum_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))