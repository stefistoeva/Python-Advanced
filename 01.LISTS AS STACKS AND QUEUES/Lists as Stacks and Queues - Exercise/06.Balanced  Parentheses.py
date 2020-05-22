parentheses = input()

fail = False
s = []
for current in parentheses:
    if current == "(" or current == "{" or current == "[":
        s.append(current)
    else:
        if not s:
            fail = True
            break
        last_opening = s.pop()
        if last_opening == "(" and current == ")" or last_opening == "[" and current == "]" or last_opening == "{" and current == "}":
            continue
        else:
            fail = True
            break

if fail:
    print("NO")
else:
    print("YES")


