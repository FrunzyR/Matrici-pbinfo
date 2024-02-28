def read():
    matrix = []
    first_line = input().split()
    number = int(first_line[0])
    return number


def solve(n):
    new_list = []
    for i in range(n):
        new_row = []
        for j in range(n):
            if i == j:
                new_row.append(0)
            elif j == 0:
                new_row.append(n)
            else:
                new_row.append(n-j)
        new_list.append(new_row)
    return new_list


def pretty_print_matrix(matrix):
    to_return = ""
    for row in matrix:
        new_row_string = " ".join(map(str, row))
        to_return += new_row_string + "\n"
    return to_return


if __name__ == "__main__":
    n = read()
    print(pretty_print_matrix(solve(n)).strip())