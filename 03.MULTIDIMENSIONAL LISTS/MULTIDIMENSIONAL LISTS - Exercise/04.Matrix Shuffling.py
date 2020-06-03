# def is_valid(pos, col, rows, cols):
#     return 0 <= pos[0] < rows and 0 <= col < cols
#
#
# (rows_count, columns_count) = [int(x) for x in input().split()]
# matrix = []
#
# for _ in range(rows_count):
#     matrix.append([int(x) for x in input().split()])
#
# line = input().split()
# while line[0] != "END":
#     if line[0] == "swap" and len(line) == 5:
#         first_element_pos = [int(line[1]), int(line[2])]
#         second_element_pos = [int(line[3]), int(line[4])]
#
#         if is_valid(first_element_pos, rows, cols) and is_valid(second_element_pos):
#             matrix[first_element_pos[0]][first_element_pos[1]], matrix[second_element_pos[0]][second_element_pos[1]] =
#     else:
#         print("Invalid input")
#     line = input().split()