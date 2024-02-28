def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def solve(matrix):
    n = len(matrix)
    magic_square = sum(matrix[0])

    for row in matrix:
        if sum(row) != magic_square:
            return False

    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != magic_square:
            return False

    if sum(matrix[i][i] for i in range(n)) != magic_square:
        return False

    if sum(matrix[i][n - i - 1] for i in range(n)) != magic_square:
        return False

    return True


if __name__ == "__main__":
    a = read()
    if solve(a):
        print("true")
    else:
        print("false")