phonebook = {}

while True:
    contact = input().split("-")
    if len(contact) == 1:
        break
    name = contact[0]
    number = contact[1]
    phonebook[name] = number

n = int(contact[0])

for _ in range(n):
    name = input()
    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
