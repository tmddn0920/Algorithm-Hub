n = int(input())
arr = input()
intarr = arr.split()
minnum = intarr[0]
maxnum = intarr[0]
for i in range(1, n):
    if int(intarr[i]) < int(minnum):
        minnum = intarr[i]
    elif int(intarr[i]) > int(maxnum):
        maxnum = intarr[i]
print(minnum + " " + maxnum)