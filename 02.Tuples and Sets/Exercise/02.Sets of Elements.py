def save_element(count):
    number_set = set()
    [number_set.add(int(input())) for _ in range(count)]
    return number_set


(n, m) = input().split(" ")
result = save_element(int(n)) & save_element(int(m))
[print(number) for number in result]
