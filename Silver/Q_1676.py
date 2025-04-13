num = int(input())
count_two = 0
count_five = 0
for i in range(1, num + 1):
    while i % 5 == 0 or i % 2 == 0:
        if i % 5 == 0:
            i = i // 5
            count_five += 1
        if i % 2 == 0:
            i = i // 2
            count_two += 1
print(min(count_two, count_five))