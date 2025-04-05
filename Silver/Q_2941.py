text = input()
count = 0
i = 0
while i < len(text):
    if text[i] == 'c':
        if i + 1 < len(text) and (text[i + 1] == '=' or text[i + 1] == '-'):
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    elif text[i] == 'd':
        if i + 1 < len(text) and text[i + 1] == '-':
            count += 1
            i += 2
        elif i + 2 < len(text) and text[i + 1] == 'z' and text[i + 2] == '=':
            count += 1
            i += 3
        else:
            count += 1
            i += 1
    elif text[i] == 'l' or text[i] == 'n':
        if i + 1 < len(text) and text[i + 1] == 'j':
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    elif text[i] == 's' or text[i] == 'z':
        if i + 1 < len(text) and text[i + 1] == '=':
            count += 1
            i += 2
        else:
            count += 1
            i += 1
    else:
        count += 1
        i += 1
print(count)