score_arr = []
for num in range(1, 9):
    score_arr.append([int(input()), num])
score_arr.sort(reverse=True)
result = 0
for num in range(0, 5):
    result += score_arr[num][0]
print(result)
arr = []
for num in range(0, 5):
    arr.append(score_arr[num][1])
arr.sort()
for num in arr:
    print(num, end=" ")