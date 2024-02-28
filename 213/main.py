def read():
    first_line = input().split()
    rows = int(first_line[0])
    return rows


def solve(rows):
    new_list = []
    for i in range(1, rows+1):
        new_row = []
        for j in range(1, rows+1):
            if i*j >= 10:
                new_row.append((i * j) % 10)
            else:
                new_row.append(i * j)
        new_list.append(new_row)
    return new_list


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return.strip()


if __name__ == "__main__":
    rows = read()
    print(pretty_print_matrix(solve(rows)))