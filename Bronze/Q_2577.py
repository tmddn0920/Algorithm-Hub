a = int(input())
b = int(input())
c = int(input())
num = a * b * c
str_num = str(num)
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(0, len(str_num)):
    arr[int(str_num[i])] += 1
for i in range(0, len(arr)):
    print(arr[i])