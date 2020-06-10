def length_symbol(text):
    count = 0
    for el in line:
        if el in "',.!?-":
            count += 1
    return count


result = ''
with open('text.txt', 'r') as file:
    for index, line in enumerate(file):
        length_line = len([el for el in line if el.isalpha()])
        length_sy = length_symbol(line)
        result += f"Line{index + 1}: {line[:-2]} ({length_line})({length_sy})\n"

with open('output.txt', 'w') as output_file:
    output_file.write(result)
