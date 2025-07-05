import math
Min, Max = map(int, input().split())
Check = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    num = i * i
    index = int(Min / num)
    if Min % num != 0:
        index += 1
    for j in range(index, int(Max / num) + 1):
        Check[int((j * num) - Min)] = True

result = 0
for i in range(len(Check)):
    if not Check[i]:
        result += 1
        
print(result)