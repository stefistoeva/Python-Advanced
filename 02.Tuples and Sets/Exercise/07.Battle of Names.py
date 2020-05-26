def print_result(set_for_print):
    return ', '.join([str(x) for x in set_for_print])


n = int(input())

odd_names = set()
even_names = set()

for index in range(1, n + 1):
    name = input()
    sum_of_ascii_values = sum([ord(x) for x in name]) // index
    if index % 2:
        even_names.add(sum_of_ascii_values)
    else:
        odd_names.add(sum_of_ascii_values)

if sum(odd_names) == sum(even_names):
    print(print_result(odd_names | even_names))
elif sum(odd_names) > sum(even_names):
    print(print_result(odd_names - even_names))
else:
    print(print_result(odd_names ^ even_names))
