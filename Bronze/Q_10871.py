n, x = map(int, input().split())
arr = input()
intarr = arr.split()
result = ""
for i in range(0, n):
    if int(intarr[i]) < x:
        result += intarr[i] + " "
print(result)