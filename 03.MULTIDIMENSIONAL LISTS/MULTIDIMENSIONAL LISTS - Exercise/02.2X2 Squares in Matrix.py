def fill_a_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


def find_squares_of_equal_chars(matrix):
    find = 0
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[row]) - 1):
            current = matrix[row][col]
            if matrix[row][col + 1] == current and matrix[row + 1][col] == current and matrix[row + 1][col + 1] == current:
                find += 1
    return find


(rows_count, columns_count) = [int(x) for x in input().split()]
matrix = fill_a_matrix(rows_count)
print(find_squares_of_equal_chars(matrix))