import sys
N, start_city, end_city, M = map(int, input().split())
Arr = []
distance = [-sys.maxsize] * N

for i in range(M):
    A, B, C = map(int, input().split())
    Arr.append((A, B, C))
    
cost = list(map(int, input().split()))

distance[start_city] = cost[start_city]

for i in range(N + 100):
    for start, end, weight in Arr:
        if distance[start] == -sys.maxsize:
            continue
        elif distance[start] == sys.maxsize:
            distance[end] = sys.maxsize
        elif distance[end] < distance[start] + cost[end] - weight:
            distance[end] = distance[start] + cost[end] - weight
            if i >= N - 1:
                distance[end] = sys.maxsize
                
if distance[end_city] == -sys.maxsize:
    print('gg')
elif distance[end_city] == sys.maxsize:
    print('Gee')
else:
    print(distance[end_city])