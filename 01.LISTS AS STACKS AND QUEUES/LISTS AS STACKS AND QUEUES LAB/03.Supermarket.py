from collections import deque

people = deque()

while True:
    name = input()

    if name == "End":
        break
    if name == "Paid":
        [print(person) for person in people]
        people = deque()
        continue

    people.append(name)

print(f"{len(people)} people remaining.")
