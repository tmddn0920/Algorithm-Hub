num = int(input())
if num > 3:
    result = num * (num - 1) * (num - 2) * (num - 3) // 24
    print(result)
else:
    print(0)