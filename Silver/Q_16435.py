N, L = map(int, input().split())
Fruit = list(map(int, input().split()))
Fruit.sort()
for Num in range(N):
    if L >= Fruit[Num]:
        L += 1
    elif L < Fruit[Num]:
        break
print(L)