from itertools import combinations

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

N, M = map(int, input().split())
A = []

for _ in range(N):
    A.append(list(map(int, input().split()))) 

cor_chicken = []
cor_house = []

for i in range(N):
    for j in range(N):
        if A[i][j] == 1:
            cor_house.append((i, j))
        if A[i][j] == 2:
            cor_chicken.append((i, j))
            
cor_chicken = list(combinations(cor_chicken, M))
total_distance = 10000


for i in range(len(cor_chicken)):
    city_distance = 0
    for j in range(len(cor_house)):
        min_distance = 10000
        hc, hr = cor_house[j]
        for k in range(len(cor_chicken[i])):
            cc, cr = cor_chicken[i][k]
            if distance(hc, hr, cc, cr) < min_distance:
                min_distance = distance(hc, hr, cc, cr)
        city_distance += min_distance
    total_distance = min(total_distance, city_distance)
    
print(total_distance)