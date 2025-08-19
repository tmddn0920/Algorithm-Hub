N = int(input())
X = []
Y = []

for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
    
X.append(X[0])
Y.append(Y[0])

result = 0

for i in range(N):
    result += (X[i] * Y[i + 1]) - (X[i + 1] * Y[i])
    
print(round(abs(result/2), 1))