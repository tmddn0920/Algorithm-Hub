import sys

input = sys.stdin.readline
output = sys.stdout.write

T = int(input().rstrip()) 

for _ in range(T):
    A, B = map(int, input().split()) 
    output(str(A + B) + '\n')