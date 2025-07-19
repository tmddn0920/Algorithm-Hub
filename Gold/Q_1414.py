import sys
from queue import PriorityQueue

N = int(input())
total = 0
pq = PriorityQueue()

for i in range(N):
    temp = list(input())
    for j in range(N):
        num = 0
        if 'a' <= temp[j] <= 'z':
            num = ord(temp[j]) - ord('a') + 1
        elif 'A' <= temp[j] <= 'Z':
            num = ord(temp[j]) - ord('A') + 27
        total += num
        if i != j and num != 0:
            pq.put((num, i, j))
            
parent = [0] * N

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

for i in range(N):
    parent[i] = i
    
count = 0
result = 0

while pq.qsize() > 0:
    length, start, end = pq.get()
    if find(start) != find(end):
        union(start, end)
        result += length
        count += 1
        
if count == N - 1:
    print(total - result)
else:
    print(-1)