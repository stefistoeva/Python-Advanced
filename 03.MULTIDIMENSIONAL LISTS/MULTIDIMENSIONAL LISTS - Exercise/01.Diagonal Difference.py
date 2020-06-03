def fill_a_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([int(x) for x in input().split()])
    return matrix


def get_primary_diagonal_sum(matrix):
    sum = 0
    for row in range(len(matrix)):
        sum += matrix[row][row]
    return sum


def get_secondary_diagonal_sum(matrix):
    sum = 0
    row = len(matrix)
    while True:
        row -= 1
        sum += matrix[row][len(matrix) - row - 1]
        if row == 0:
            break
    return sum


def difference(primary_diagonal, secondary_diagonal):
    return abs(primary_diagonal - secondary_diagonal)


size_of_matrix = int(input())
matrix = fill_a_matrix(size_of_matrix)
primary_diagonal_sum = get_primary_diagonal_sum(matrix)
secondary_diagonal_sum = get_secondary_diagonal_sum(matrix)
print(difference(primary_diagonal_sum, secondary_diagonal_sum))
