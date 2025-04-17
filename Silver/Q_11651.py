num = int(input())
arr = []
for i in range(0, num):
    x, y = map(int, input().split())
    arr.append([x, y])
sorted_arr = sorted(arr, key=lambda x: [x[1], x[0]])
for i in range(0, num):
    print(sorted_arr[i][0], end=" ")
    print(sorted_arr[i][1])