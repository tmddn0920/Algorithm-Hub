num = int(input())
count = 0
for i in range(0, num):
    str = input()
    arr = []
    for i in range(0, len(str)):
        if str[i] not in arr:
            arr.append(str[i])
        elif str[i] in arr and str[i - 1] != str[i]:
            count -= 1
            break
    count += 1
print(count)