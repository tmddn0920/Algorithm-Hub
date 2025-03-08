H, M = map(int, input().split(" "))
if (M >= 45):
    print(H, M - 45)
else:
    H = H - 1 if H > 0 else 23
    print(H, M + 15)