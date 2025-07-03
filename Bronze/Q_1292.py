A, B = map(int, input().split())

Arr = []
count = 1
while len(Arr) < B:
    Arr += [count] * count
    count += 1

print(sum(Arr[A-1:B]))