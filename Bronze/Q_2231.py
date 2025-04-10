num = int(input())
result = 0

for i in range(1, num + 1):
    digits_sum = sum(map(int, str(i)))
    if i + digits_sum == num:
        result = i
        break

print(result)