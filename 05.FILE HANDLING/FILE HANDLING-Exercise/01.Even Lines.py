def change_symbol(text):
    original_symbol = {"-", ",", ".", "!", "?"}
    for symbol in original_symbol:
        text = text.replace(symbol, "@")
    return text


with open('text.txt') as file:
    for index, line in enumerate(file):
        if index % 2 == 0:
            line = change_symbol(line)
            word_dictionary = reversed(line.split())
            print(' '.join(word_dictionary))
