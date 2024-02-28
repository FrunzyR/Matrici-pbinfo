def read():
    the_number = int(input())
    return the_number


def solve(number):
    matrix = []
    for i in range(number):
        new_row = []
        for j in range(number):
            if (i+1) % 2 == 1:
                new_row.append(i+1)
            else:
                new_row.append(j+1)
        matrix.append(new_row)
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