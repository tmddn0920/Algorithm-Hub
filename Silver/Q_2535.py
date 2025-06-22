N = int(input())
Students = []

for _ in range(N):
    Students.append(list(map(int, input().split())))

Students.sort(key=lambda x: x[2], reverse = True)

Winner = []
Count = {}

for A, B, C in Students:
    if Count.get(A, 0) >= 2:
        continue
    Winner.append((A, B))
    Count[A] = Count.get(A, 0) + 1
    
    if len(Winner) == 3:
        break

for A, B in Winner:
    print(A, B)