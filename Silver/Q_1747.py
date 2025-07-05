import math

N = int(input())
A = [0] * 10000001

for i in range(2, 10000001):
    A[i] = i
    
for i in range(2, int(math.sqrt(10000001) + 1)):
    if A[i] == 0:
        continue
    for j in range(i + i, 10000001, i):
        A[j] = 0

def isPalindrome(num):
    temp = list(str(num))
    s = 0
    e = len(temp) - 1
    while s < e:
        if temp[s] != temp[e]:
            return False
        s += 1
        e -= 1
    return True

i = N
while True:
    if A[i] != 0 and isPalindrome(A[i]):
        print(A[i])
        break
    i += 1