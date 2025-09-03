import sys
from queue import PriorityQueue
input = sys.stdin.readline
sys.setrecursionlimit(100000)

V, E = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (V + 1)

for i in range(V + 1):
    parent[i] = i

for i in range(E):
    start, end, weight = map(int, input().split())
    pq.put((weight, start, end))
    
def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
count = 0
result = 0
max_edge = 0

while count < V - 1:
    weight, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += weight
        if weight > max_edge:
            max_edge = weight
        count += 1
        
print(result - max_edge)