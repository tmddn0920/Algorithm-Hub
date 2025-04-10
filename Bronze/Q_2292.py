num = int(input())
count = 0
num = num - 1
while num > 6 * count:
    num -= 6 * count
    count += 1
print(count + 1)