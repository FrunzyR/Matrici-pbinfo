def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def even(lista):
    sum_row = 0
    for element in lista:
        if element % 2 == 0:
            sum_row += element
    return sum_row


def solve(matrix):
    even_total_numbers = 0
    for row in matrix:
        even_total_numbers += even(row)
    return even_total_numbers


if __name__ == "__main__":
    a = read()
    print(solve(a))
    