(rows_count, columns_count) = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split()])

columns_sum = [0] * columns_count

for row in range(rows_count):
    for col in range(columns_count):
        columns_sum[col] += matrix[row][col]

[print(x) for x in columns_sum]
