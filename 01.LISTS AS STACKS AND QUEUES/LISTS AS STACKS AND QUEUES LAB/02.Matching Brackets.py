expression = input()


def get_subexpression(exp):
    s = []
    result = []
    for index in range(len(exp)):
        if exp[index] == '(':
            s.append(index)
        elif exp[index] == ')':
            start_index = s.pop()
            result.append(exp[start_index:index + 1])
    return result


print("\n".join(get_subexpression(expression)))
