def read():
    the_number = int(input())
    return the_number


def solve(number):
    matrix = [[0]*number for _ in range(number)]
    current_number = 2
    for i in range(number):
        for j in range(number):
            if current_number % 2 == 0 and current_number % 3 != 0:
                matrix[i][j] = current_number
                current_number += 2
            else:
                current_number += 2
                if current_number % 2 == 0 and current_number % 3 != 0:
                    matrix[i][j] = current_number
                    current_number += 2

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
    