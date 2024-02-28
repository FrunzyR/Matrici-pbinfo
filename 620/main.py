def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def sort_arc(row):
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] >= row[j]:
                row[i], row[j] = row[j], row[i]
    return row


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


def solve(matrix):
    new_list = []
    for i in range(len(matrix)):
        if sort_arc(matrix[i]):
            new_list.append(sort_arc(matrix[i]))
    new_list = rotate_matrix(new_list)

    return new_list


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return


if __name__ == "__main__":
    a = read()
    result = rotate_matrix(a)
    result.reverse()

    print(pretty_print_matrix(solve(result)).strip())