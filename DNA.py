def get_repeating_DNA(string):
    repeating = []
    if len(string) <= 10:
        return repeating

    current = [string[:10]]
    for i in range(1, len(string) - 9):
        if string[i:i + 10] in current and string[i:i + 10] not in repeating:
            repeating.append(string[i:i + 10])
        current.append(string[i:i + 10])

    return repeating


test = "AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)

test = "TTCCTTAAGGCCGACTTCCAAGGTTCGATC"
result = get_repeating_DNA(test)
print(result)

test = "AAAAAAAAAAA"
result = get_repeating_DNA(test)
print(result)
