A, B = map(int, input().split())
N = int(input())
star = []
for _ in range(N):
    star.append(int(input()))
num = abs(A - B)
for i in range(len(star)):
    if abs(B - star[i]) + 1 < num:
        num = abs(B - star[i]) + 1
print(num)