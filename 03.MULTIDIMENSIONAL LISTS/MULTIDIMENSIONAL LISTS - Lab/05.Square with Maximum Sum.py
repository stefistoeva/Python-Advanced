(rows_count, columns_count) = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(', ')])

best_position = (0, 0)
best_value = matrix[0][0] + matrix[0][0 + 1] + \
           matrix[0 + 1][0] + matrix[0 + 1][0 + 1]


for row in range(len(matrix) - 2 + 1):
    for col in range(len(matrix[row]) - 2 + 1):
        current_value = matrix[row][col] + matrix[row][col + 1] + \
           matrix[row + 1][col] + matrix[row + 1][col + 1]
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)


(best_row, best_col) = best_position

for r in range(best_row, best_row + 2):
    for c in range(best_col, best_col + 2):
        print(matrix[r][c], end=' ')
    print()

print(best_value)