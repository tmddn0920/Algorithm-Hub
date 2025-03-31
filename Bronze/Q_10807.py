num = int(input())
arr = input()
intarr = arr.split()
count = 0
num_find = int(input())
for i in range(0, num):
    if int(intarr[i]) == num_find:
        count += 1
print(count)