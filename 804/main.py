def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def solve(matrix):
    iden = []
    for i in range(len(matrix[0])):
        identical = True
        for j in range(len(matrix)-1):
            if matrix[j][i] != matrix[j+1][i]:
                identical = False
        if identical:
            iden.append(str(matrix[0][i]))
    if len(iden) == 0:
        return "nu exista"
    return " ".join(iden)


if __name__ == "__main__":
    a = read()
    print(solve(a))
