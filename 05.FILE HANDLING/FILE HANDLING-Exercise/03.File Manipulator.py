import os


def create_file(name):
    with open(name, 'w') as file:
        file.write("")


def add_file(name, text):
    with open(name, 'a') as file:
        file.write(text + "\n")


def replace_string(name, old, new):
    if os.path.exists(name):
        text = ""
        with open(name, "r") as file:
            text = file.read()
        text = text.replace(old, new)
        with open(name, "w") as file:
            file.write(text)
    else:
        print("An error occurred")


def delete_file(name):
    if os.path.exists(name):
        os.remove(file_name)
    else:
        print("An error occurred")


while True:
    token = input().split("-")
    if token[0] == "End":
        break
    file_name = token[1]

    if token[0] == "Create":
        create_file(file_name)
    elif token[0] == "Add":
        content = token[2]
        add_file(file_name, content)
    elif token[0] == "Replace":
        old_string = token[2]
        new_string = token[3]
        replace_string(file_name, old_string, new_string)
    elif token[0] == "Delete":
        delete_file(file_name)
