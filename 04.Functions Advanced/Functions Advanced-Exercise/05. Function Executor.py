def func_executor(*args):
    result = []
    for element in args:
        function = element[0]
        arguments = element[1]
        result.append(function(*arguments))
    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
