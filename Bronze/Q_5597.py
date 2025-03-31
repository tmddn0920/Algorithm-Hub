arr = []
for i in range(0, 28):
    num = int(input())
    arr.append(num)
stu = []
for i in range(1, 31):
    if i in arr:
        continue
    else:
        stu.append(i)
if stu[0] > stu[1]:
    print(stu[1])
    print(stu[0])
else:
    print(stu[0])
    print(stu[1])