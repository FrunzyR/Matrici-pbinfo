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
        for j in range(i+1, len(row)):
            if row[i] >= row[j]:
                row[i], row[j] = row[j], row[i]
    return " ".join(map(str, row))


def solve(matrix):
    new_list = []
    for i in range(len(matrix)):
        if sort_arc(matrix[i]):
            new_list.append(sort_arc(matrix[i]))
    return "\n".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))