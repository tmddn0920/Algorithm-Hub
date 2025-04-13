num = int(input())
arr = []
for i in range(0, num):
    arr.append(input())
arr = sorted(arr, key=lambda x: (len(x), x))
arr_unique = []
for i in arr:
    if i not in arr_unique:
        arr_unique.append(i)
for i in range(0, len(arr_unique)):
    print(arr_unique[i])