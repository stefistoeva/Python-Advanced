def unique(tuples):
    unique_value = {}

    for number in tuples:
        if number not in unique_value:
            unique_value[number] = 0
        unique_value[number] += 1

    return unique_value


def result(unique_value):
    for (number, count) in unique_value.items():
        number = float(number)
        print(f"{number} - {count} times")


numbers = input().split(" ")
unique_values = unique(numbers)
result(unique_values)
