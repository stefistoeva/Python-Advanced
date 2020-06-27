n = int(input())

snake_game = []
snake_position = ()
food_quantity = 0
is_win = False
lair = []

for row in range(n):
    line = [x for x in input()]
    if "S" in line:
        snake_position = (row, line.index("S"))
    if "B" in line:
        lair.append((row, line.index("B")))
    snake_game.append(line)

directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
while True:
    command = input()
    row = snake_position[0]
    col = snake_position[1]
    row += int(directions[command][0])
    col += int(directions[command][1])
    snake_game[snake_position[0]][snake_position[1]] = "."

    if row >= n or row < 0 or col >= n or col < 0:
        break

    current_cell = snake_game[row][col]

    if current_cell == "B":
        snake_game[row][col] = "."

        if row == lair[0][0] and col == lair[0][1]:
            snake_position = (lair[1][0], lair[1][1])
        else:
            snake_position = (lair[0][0], lair[0][1])
        snake_game[snake_position[0]][snake_position[1]] = "S"
    elif current_cell == "*":
        food_quantity += 1
        if food_quantity >= 10:
            is_win = True
            snake_game[row][col] = "S"
            break
        snake_game[row][col] = "."
        snake_position = (row, col)

    else:
        snake_game[row][col] = "."
        snake_position = (row, col)

if is_win:
    print("You won! You fed the snake.")
else:
    print("Game over!")

print(f"Food eaten: {food_quantity}")

[print("".join(line_for_print)) for line_for_print in snake_game]
