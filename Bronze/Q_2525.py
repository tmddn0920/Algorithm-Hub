H, M = map(int, input().split())
T = int(input())

H += T // 60  
M += T % 60   

H += M // 60
M %= 60

H %= 24

print(H, M)