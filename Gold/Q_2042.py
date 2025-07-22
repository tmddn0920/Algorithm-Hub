import math

N, M, K = map(int, input().split())
height = math.ceil(math.log2(N))  
tree_size = 2 ** (height + 1)
start_index = 2 ** height
tree = [0] * tree_size

for i in range(start_index, start_index + N):
    tree[i] = int(input())
    
def createTree(num):
    while num != 1:
        tree[num // 2] += tree[num]
        num -= 1

createTree(tree_size - 1)

def changeNum(i, num):
    temp = num - tree[i]
    while i > 0:
        tree[i] = tree[i] + temp
        i = i // 2
        
def addNum(start, end):
    temp = 0
    while start <= end:
        if start % 2 == 1:
            temp += tree[start]
            start += 1
        if end % 2 == 0:
            temp += tree[end]
            end -= 1
        start = start // 2
        end = end // 2
    print(temp)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        changeNum(b + start_index - 1, c)
    elif a == 2:
        addNum(b + start_index - 1, c + start_index - 1)