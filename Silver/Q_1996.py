num = int(input())
Solve = [[0] * num for _ in range(num)]
Map = []
for _ in range(num):
    Map.append(list(input()))

def find(X, Y):
    Count = 0
    if Map[X][Y] != '.':
        Solve[X][Y] = '*'
        return
    for y in range(Y - 1, Y + 2):
        for x in range(X - 1, X + 2):
            if (x >= 0 and y >= 0) and (X != x or Y != y) and (x < num and y < num):
                if Map[x][y] != '.':
                    Count += int(Map[x][y])
        if Count >= 10:
            Solve[X][Y] = 'M'
            return
        Solve[X][Y] = Count

for Y in range(num):
    for X in range(num):
        find(X, Y)
for Row in Solve:
    for Num in Row:
        print(Num, end="")
    print()