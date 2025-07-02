from queue import PriorityQueue
N = int(input())
pq_1 = PriorityQueue()
pq_2 = PriorityQueue()
zero = 0
one = 0

for _ in range(N):
    data = int(input())
    if data > 1:
        pq_1.put(data * -1)
    elif data < 0:
        pq_2.put(data)
    elif data == 0:
        zero += 1
    else:
        one += 1

total = 0

while pq_1.qsize() > 1:
    data_1 = pq_1.get() * -1
    data_2 = pq_1.get() * -1
    total += data_1 * data_2

if pq_1.qsize() == 1:
    total += pq_1.get() * -1

while pq_2.qsize() > 1:
    data_1 = pq_2.get() 
    data_2 = pq_2.get()
    total += data_1 * data_2

if pq_2.qsize() == 1:
    if zero == 0:
        total += pq_2.get()

total += one 
print(total)       