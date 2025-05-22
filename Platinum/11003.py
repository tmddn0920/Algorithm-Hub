from collections import deque

N, L = map(int, input().split())
Now = list(map(int, input().split()))
myDeque = deque()

for i in range(N):
    while myDeque and myDeque[-1][0] > Now[i]:
        myDeque.pop()
    myDeque.append([Now[i], i])
    if myDeque[0][1] <= i - L:
        myDeque.popleft()
    print(myDeque[0][0], end=" ")