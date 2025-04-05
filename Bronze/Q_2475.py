line = input()
arr = line.split()
result = 0
for i in arr:
    result += int(i) * int(i)
print(result % 10)