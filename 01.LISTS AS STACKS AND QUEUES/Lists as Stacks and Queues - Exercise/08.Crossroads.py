from collections import deque

green_time = int(input())
yellow_time = int(input())
crashed = False


cars = deque()
counter = 0

line = input()
while line.upper() != "END":
    if line == "green":
        timer = green_time
        if cars:
            copy = cars.popleft()
            current = deque(copy)
            while timer:
                if not current:
                    if cars:
                        copy = cars.popleft()
                        current = deque(copy)
                    else:
                        break
                current.popleft()
                timer -= 1
            if current:
                yellow_timer = yellow_time
                while yellow_time and current:
                    current.popleft()
                    yellow_time -= 1
            if current:
                crashed = True
                print("A crash happened!")
                print(f"{copy} was hit at {current.popleft()}.")
                break
    else:
        cars.append(line)
        counter += 1

    line = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{counter - len(cars)} total cars passed the crossroads.")