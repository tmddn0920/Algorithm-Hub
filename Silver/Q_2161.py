from collections import deque

dq = deque()

num = int(input())
for i in range(1, num + 1):
    dq.append(i)

arr = []
    
while len(dq) > 1:
    arr.append(dq[0])
    dq.popleft()
    dq.append(dq[0])
    dq.popleft()
    
for i in range(len(arr)):
    print(arr[i], end = " ")
print(dq[0])
    
    

