def fill_a_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append([x for x in input().split()])
    return matrix


(rows_count, columns_count) = [int(x) for x in input().split()]
matrix = fill_a_matrix(rows_count)

best_sum = -99999999
best_matrix = []
for row in range(rows_count - 2):
    for col in range(columns_count - 2):
        sub_matrix = []
        sum = 0
        row_counter = 0
        for r in range(row, row + 3):
            sub_matrix.append([])
            for c in range(col, col + 3):
                sub_matrix[row_counter].append(matrix[r][c])
                sum += int(matrix[r][c])
            row_counter += 1
        if best_sum < sum:
            best_sum = sum
            best_matrix = sub_matrix

print(f"Sum = {best_sum}")
for row in best_matrix:
    print(' '.join([str(x) for x in row]))
