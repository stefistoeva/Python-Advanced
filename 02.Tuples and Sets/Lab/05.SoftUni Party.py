number_of_guests = int(input())

list_of_guests = set()
for _ in range(number_of_guests):
    list_of_guests.add(input())

while True:
    guest = input()
    if guest == "END":
        break
    list_of_guests.remove(guest)

result = sorted(list_of_guests)
print(len(list_of_guests))
[print(quest) for quest in result if quest[0].isdigit()]
[print(quest) for quest in result if not quest[0].isdigit()]
