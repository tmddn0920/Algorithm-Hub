import math
N = int(input())
total = N

for i in range(2, int(math.sqrt(N) + 2)):
    if N % i == 0:
        total -= total / i
    while N % i == 0:
        N /= i
    
if N > 1:
    total -= total / N
    
print(int(total))