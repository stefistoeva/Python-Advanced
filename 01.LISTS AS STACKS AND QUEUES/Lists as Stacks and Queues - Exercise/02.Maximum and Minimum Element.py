n = int(input())

numbers = []

for _ in range(n):
    tokens = input().split()
    command = int(tokens[0])
    if command == 1:
        numbers.append(int(tokens[1]))
    elif command == 2 and numbers:
        numbers.pop()
    elif command == 3 and numbers:
        print(max(numbers))
    elif command == 4 and numbers:
        print(min(numbers))

print(', '.join([str(x) for x in reversed(numbers)]))
