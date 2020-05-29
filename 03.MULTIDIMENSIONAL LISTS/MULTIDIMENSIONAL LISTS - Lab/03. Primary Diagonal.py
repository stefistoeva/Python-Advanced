size_of_matrix = int(input())
matrix = []

for _ in range(size_of_matrix):
    matrix.append([int(x) for x in input().split()])

primary_diagonal_sum = 0
for row in range(size_of_matrix):
    primary_diagonal_sum += matrix[row][row]

print(primary_diagonal_sum)