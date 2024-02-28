def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def remove_nth_row(matrix, n):
    new_matrix = []
    for i in range(len(matrix)):
        if i == n:
            continue
        new_matrix.append(matrix[i])
    return new_matrix


def remove_nth_column(matrix, n):
    new_matrix =[]
    for row in matrix:
        new_row =[]
        for i in range(len(row)):
            if i == n:
                continue
            new_row.append(row[i])
        new_matrix.append(new_row)
    return new_matrix


def solve(matrix):
    matrix = remove_nth_row(matrix, len(matrix)-2)
    matrix = remove_nth_column(matrix, len(matrix[0])-2)

    return matrix


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return


if __name__ == "__main__":
    a = read()
    result = solve(a)
    print(pretty_print_matrix(result).strip())

