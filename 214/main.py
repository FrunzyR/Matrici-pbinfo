def read():
    first_line = input().split()
    the_number = int(first_line[0])
    return the_number


def solve(number):
    n = len(str(number))
    matrix = [[0]*n for _ in range(n)]
    for i in range(n):
        digit = number % 10
        number //= 10
        for j in range(n):
            matrix[j][i] = digit

    return matrix


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return.strip()


if __name__ == "__main__":
    numbers = read()
    print(pretty_print_matrix(solve(numbers)))
    