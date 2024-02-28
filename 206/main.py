def read():
    first_line = input().split()
    row = int(first_line[0])
    column = int(first_line[1])
    return row, column


def solve(r, c):
    new_list = []
    for i in range(r):
        new_row = []
        for j in range(c):
            if i <= j:
                new_row.append(i+1)
            else:
                new_row.append(j+1)
        new_list.append(new_row)
    return new_list


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return.strip()


if __name__ == "__main__":
    r, c = read()
    print(pretty_print_matrix(solve(r, c)))