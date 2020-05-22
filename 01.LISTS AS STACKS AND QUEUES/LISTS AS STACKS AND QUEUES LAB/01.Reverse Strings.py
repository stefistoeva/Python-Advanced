text = input()
string = []
for letter in text:
    string.append(letter)

reversed_string = []
while string:
    reversed_string.append(string.pop())

print(''.join(reversed_string))

# The pythonic way
# print(text[::-1])
