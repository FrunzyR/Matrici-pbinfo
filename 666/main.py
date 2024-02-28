from math import sqrt


def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    # column = int(first_line[1])
    for i in range(1, row+1):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if n == 3:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def even_index(matrix):
    cont = 0
    for i in range(1, len(matrix)+1):
        if i % 2 == 0:
            for j in range(1, len(matrix[i-1])+1):
                if is_prime(matrix[i-1][j-1]):
                    cont += 1
    return cont


if __name__ == "__main__":
    a = read()
    print(even_index(a))
    