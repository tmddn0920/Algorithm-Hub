def change(arr, a, b):
    new_arr = arr[a - 1:b]
    new_arr.reverse()
    for num in range(a - 1, b):
        arr[num] = new_arr[num - a + 1]
        
n, m = map(int, input().split())
arr = []
for num in range(1, n + 1):
    arr.append(num)
for num in range(0, m):
    a, b = map(int, input().split())
    change(arr, a, b)
for num in arr:
    print(num, end=" ")