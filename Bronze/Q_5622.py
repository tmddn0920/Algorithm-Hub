line = input()
result = 0
for i in line:
    if i in ["A", "B", "C"]:
        result = result + 3
    elif i in ["D", "E", "F"]:
        result = result + 4
    elif i in ["G", "H", "I"]:
        result = result + 5
    elif i in ["J", "K", "L"]:
        result = result + 6
    elif i in ["M", "N", "O"]:
        result = result + 7
    elif i in ["P", "Q", "R", "S"]:
        result = result + 8
    elif i in ["T", "U", "V"]:
        result = result + 9
    elif i in ["W", "X", "Y", "Z"]:
        result = result + 10
print(result)
        