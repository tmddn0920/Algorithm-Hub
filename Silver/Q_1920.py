n = int(input())
intarr = set(input().split())
m = int(input())
find = input().split()
for i in find:
    print(1 if i in intarr else 0)