n = int(input())

records = set()
for _ in range(n):
    records.add(input())

[print(name) for name in records]
