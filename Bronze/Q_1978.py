import math

def isDevide(n):
    result = True
    if n == 1:
        result = False
    test_n = int(math.sqrt(n)) + 1
    for i in range(2, test_n + 1):
        if n % i == 0:
            result = False
    if n == 2:
        result = True
    return result

num = int(input())
count = 0
test = list(map(int, input().split()))
for i in test:
    if isDevide(i) == True:
        count += 1

print(count)