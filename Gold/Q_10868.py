import sys
import math

N, M = map(int, input().split())
height = math.ceil(math.log2(N))  # 정확한 높이
tree_size = 2 ** (height + 1)
start_index = 2 ** height
tree = [sys.maxsize] * tree_size

for i in range(start_index, start_index + N):
    tree[i] = int(input())
    
def createTree(num):
    while num != 1:
        if tree[num // 2] > tree[num]:
            tree[num // 2] = tree[num]
        num -= 1

createTree(tree_size - 1)
        
def getMin(start, end):
    temp = sys.maxsize
    while start <= end:
        if start % 2 == 1:
            temp = min(temp, tree[start])
            start += 1
        if end % 2 == 0:
            temp = min(temp, tree[end])
            end -= 1
        start = start // 2
        end = end // 2
    print(temp)

for _ in range(M):
    start, end = map(int, input().split())
    start = start + start_index - 1
    end = end + start_index - 1
    getMin(start, end)