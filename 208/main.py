def read():
    matrix = []
    first_line = input().split()
    rows = int(first_line[0])
    columns = int(first_line[1])
    return rows, columns


def squared(n):
    if n % 2 == 1:
        return n * n


def solve(row, column):
    new_list = []
    current_number = 1
    for i in range(row):
        new_row = []
        for j in range(column):
            new_row.append(squared(current_number))
            current_number += 2
        new_list.append(new_row)
    return new_list


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return.strip()


if __name__ == "__main__":
    row, column = read()
    print(pretty_print_matrix(solve(row, column)))
