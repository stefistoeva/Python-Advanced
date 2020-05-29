size_of_matrix = int(input())
matrix = []

for _ in range(size_of_matrix):
    matrix.append(input())

symbol = input()
position = ()

for row in range(size_of_matrix):
    word = matrix[row]
    if symbol in word:
        position = (row, word.index(symbol))
        break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")