import sys
input = sys.stdin.readline

n, k = map(int, input().split())
worth = []
count = 0

for i in range(n):
    coin = int(input())
    worth.append(coin)
    
for i in range(1, n + 1):
    if k // worth[-i] != 0:
        count += k // worth[-i]
        k = k % worth[-i]

print(count)
        