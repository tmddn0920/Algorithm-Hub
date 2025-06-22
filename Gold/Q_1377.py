import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))
    
A_Sorted = sorted(A)
Max = 0

for i in range(N):
    if A_Sorted[i][1] - i > Max:
        Max = A_Sorted[i][1] - i
        
print(Max + 1)