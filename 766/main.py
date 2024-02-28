def read():
    matrix = []
    first_line = input().split()
    row = int(first_line[0])
    for i in range(row):
        number_line = input().split()
        matrix.append([int(x) for x in number_line])
    return matrix


def cont_even(lista):
    cont = 0
    for element in lista:
        if element % 2 == 0:
            cont += 1
    return cont


def solve(matrix):
    even_per_row = []
    for i in range(len(matrix)):
        even_per_row.append(cont_even(matrix[i]))
    return even_per_row


def maxim(matrix):
    maximum_list = solve(matrix)
    maxi = -1
    list_of_maximum_indices = []
    for i in range(len(maximum_list)):
        if maximum_list[i] > maxi:
            maxi = maximum_list[i]
            list_of_maximum_indices = []
        if maximum_list[i] == maxi:
            list_of_maximum_indices.append(str(i + 1))

    return " ".join(list_of_maximum_indices)


if __name__ == "__main__":
    a = read()
    print(maxim(a))
