from collections import deque

quantity_of_water = int(input())
people = deque()

while True:
    name = input()
    if name == "Start":
        break
    people.append(name)

while True:
    token = input().split()
    if token[0] == "End":
        break

    if token[0] == "refill":
        quantity_of_water += int(token[1])
    else:
        need_water = int(token[0])
        current_person = people.popleft()
        if need_water <= quantity_of_water:
            print(f"{current_person} got water")
            quantity_of_water -= need_water
        else:
            print(f"{current_person} must wait")
            people.append(current_person)

print(f"{quantity_of_water} liters left")