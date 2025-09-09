import sys
input = sys.stdin.readline

R, C = map(int, input().split())
A = []
result = 0
alpha = [False] * 26
dr_r = [0, 1, 0, -1]
dr_c = [1, 0, -1, 0]

for _ in range(R):
    A.append(list(input()))

def DFS(r, c, depth):
    global result
    if depth > result:
        result = depth
    for i in range(4):
        nr, nc = r + dr_r[i], c + dr_c[i]
        if 0 <= nr < R and 0 <= nc < C:
            ch = A[nr][nc]
            num = ord(ch) - 65
            if not alpha[num]:
                alpha[num] = True            
                DFS(nr, nc, depth + 1)
                alpha[num] = False      

alpha[ord(A[0][0]) - 65] = True
DFS(0, 0, 1)
print(result)