N = int(input())
A, B, C = map(int, input().split())
max_left, max_mid, max_right = A, B, C
min_left, min_mid, min_right = A, B, C

for _ in range(N - 1):
    A, B, C = map(int, input().split())

    nmax_left  = max(A + max_left, A + max_mid)
    nmax_mid   = max(B + max_left, B + max_mid, B + max_right)
    nmax_right = max(C + max_mid, C + max_right)

    nmin_left  = min(A + min_left, A + min_mid)
    nmin_mid   = min(B + min_left, B + min_mid, B + min_right)
    nmin_right = min(C + min_mid, C + min_right)

    max_left, max_mid, max_right = nmax_left, nmax_mid, nmax_right
    min_left, min_mid, min_right = nmin_left, nmin_mid, nmin_right

print(max(max_left, max_mid, max_right), min(min_left, min_mid, min_right))