def list_manipulator(amount, command, operation, *args):
    result = amount
    if command == "add" and operation == "beginning":
        [result.insert(0, x) for x in args[::-1]]
    elif command == "add" and operation == "end":
        [result.append(x) for x in args]
    elif command == "remove" and operation == "beginning":
        if args:
            del result[0:args[0]]
        else:
            result.pop(0)
    elif command == "remove" and operation == "end":
        if args:
            del result[len(result) - args[0]:]
        else:
            result.pop()
    return result


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))