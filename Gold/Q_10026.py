import sys
sys.setrecursionlimit(10000)

N = int(input())
Picture = []
for _ in range(N):
    Picture.append(list(input()))

import copy
GRPicture = copy.deepcopy(Picture)

for y in range(N):
    for x in range(N):
        if GRPicture[y][x] == 'R':
            GRPicture[y][x] = 'G'

def find(x, y):
    global Picture
    color = Picture[y][x]
    Picture[y][x] = 0  
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if Picture[ny][nx] == color:
                find(nx, ny)

def GR_find(x, y):
    global GRPicture
    color = GRPicture[y][x]
    GRPicture[y][x] = 0
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if GRPicture[ny][nx] == color:
                GR_find(nx, ny)

Count = 0
for y in range(N):
    for x in range(N):
        if Picture[y][x] in ('R', 'G', 'B'):
            find(x, y)
            Count += 1
Result_Normal = Count

Count = 0
for y in range(N):
    for x in range(N):
        if GRPicture[y][x] in ('G', 'B'):
            GR_find(x, y)
            Count += 1
Result_GR = Count

print(Result_Normal, end = " ")
print(Result_GR)