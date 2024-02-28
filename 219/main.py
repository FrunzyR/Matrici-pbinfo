def read():
    first_line = input().split()
    rows = int(first_line[0])
    columns = int(first_line[1])
    return rows, columns


def solve(row, column):
    matrix = []
    number = row * column
    for i in range(row):
        new_row = []
        for j in range(column):
            new_row.append(number)
            number -= 1
        matrix.append(new_row)
    return matrix


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return.strip()


if __name__ == "__main__":
    row, column = read()
    print(pretty_print_matrix(solve(row, column)))
