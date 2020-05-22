from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current = orders.popleft()
    if food_quantity >= current:
        food_quantity -= current
    else:
        orders.appendleft(current)
        print(f"Orders left: {' '.join([str(x) for x in orders])}")
        break
else:
    print("Orders complete")
