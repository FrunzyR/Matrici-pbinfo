def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def solve(matrix):
    cont = 0
    for i in range(len(matrix)-1):
        for j in range(i+1, len(matrix)):
            if matrix[i] == matrix[j]:
                cont += 1

    if cont == 0:
        return "NU EXISTA"
    return cont


if __name__ == "__main__":
    a = read()
    print(solve(a))