clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())

count_of_rack = 0

current_rack = 0

while clothes:
    current = clothes.pop()
    if current_rack + current <= capacity_of_rack:
        current_rack += current
        if not clothes:
            count_of_rack += 1
    else:
        count_of_rack += 1
        current_rack = 0
        clothes.append(current)

print(count_of_rack)
