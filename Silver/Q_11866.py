n, k = map(int, input().split())
queue = []
result = []

for i in range(1, n + 1):
    queue.append(i)
while len(queue) != 0:
    num = (k - 1) % len(queue)
    result.append(queue[num])
    queue.pop(num)
    queue[:] = queue[num:] + queue[:num]
print("<", end="")
for i in range(len(result) - 1):
    print(result[i], end=", ")
print(result[len(result) - 1], end=">")
    
    