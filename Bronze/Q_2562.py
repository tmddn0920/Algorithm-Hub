arr = []
for i in range(0, 9):
    num = int(input())
    arr.append(num)
index = 0
for i in range(1, 9):
    if int(arr[i]) > int(arr[index]):
        index = i
print(arr[index])
print(index + 1)