length = int(input())
arr = [64, 32, 16, 8, 4, 2, 1]
count = 0

for num in arr:
    if length >= num:
        length -= num
        count += 1

print(count)