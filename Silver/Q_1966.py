from collections import deque

num = int(input())
for _ in range(num):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque(enumerate(arr))
    count = 0
    while True:
        if q[0][1] == max(q, key=lambda x: x[1])[1]:
            idx, val = q.popleft()
            count += 1
            if idx == m:
                print(count)
                break
        else:
            q.append(q.popleft())