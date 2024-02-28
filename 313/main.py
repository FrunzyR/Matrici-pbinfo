def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def diagonala_principala(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][i]
    return diagonal_sum


def diagonala_secundara(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][n - i - 1]
    return diagonal_sum


def solve(matrix):
    return abs(diagonala_principala(matrix) - diagonala_secundara(matrix))


if __name__ == "__main__":
    a = read()
    print(solve(a))
