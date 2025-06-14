num = int(input())
paper = [[0]* 100 for _ in range(100)]

for _ in range(num):
    x, y = map(int, input().split())
    for Y in range(y - 1, y + 9):
        for X in range(x - 1, x + 9):
            paper[X][Y] = 1
            
count = 0
for Y in range(100):
    for X in range(100):
        if paper[X][Y] == 1:
            count += 1
print(count)