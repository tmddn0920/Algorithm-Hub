from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    pq.put(int(input()))
    
data_1 = 0
data_2 = 0
total = 0

while pq.qsize() > 1:
    data_1 = pq.get()
    data_2 = pq.get()
    temp = data_1 + data_2
    total += temp
    pq.put(temp)

print(total)