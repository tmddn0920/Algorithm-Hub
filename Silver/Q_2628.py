X, Y = map(int, input().split())
N = int(input())
Arr_X = []
Arr_Y = []
for _ in range(N):
    A, B = map(int, input().split())
    if A == 1:
        Arr_X.append(B)
    if A == 0:
        Arr_Y.append(B)
Arr_X.append(X)
Arr_Y.append(Y)
Arr_X.sort()
Arr_Y.sort()
Max_X = Arr_X[0]
Max_Y = Arr_Y[0]
if len(Arr_X) > 1:
    for i in range(1, len(Arr_X)):
        if Arr_X[i] - Arr_X[i - 1] > Max_X:
            Max_X = Arr_X[i] - Arr_X[i - 1]
if len(Arr_Y) > 1:
    for i in range(1, len(Arr_Y)):
        if Arr_Y[i] - Arr_Y[i - 1] > Max_Y:
            Max_Y = Arr_Y[i] - Arr_Y[i - 1]
print(Max_X * Max_Y)