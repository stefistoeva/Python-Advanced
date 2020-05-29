(rows_count, columns_count) = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append([int(x) for x in input().split(', ')])

sum_of_matrix = sum((sum(row) for row in matrix))
print(sum_of_matrix)
print(matrix)
