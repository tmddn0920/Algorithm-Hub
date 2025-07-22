import math
import sys
input = sys.stdin.readline
MOD = 1000000007

N, M, K = map(int, input().split())
height = math.ceil(math.log2(N))  
tree_size = 2 ** (height + 1)
start_index = 2 ** height
tree = [1] * tree_size

for i in range(start_index, start_index + N):
    tree[i] = int(input())

def createTree(num):
    while num != 1:
        tree[num // 2] = (tree[num // 2] * tree[num]) % MOD
        num -= 1

createTree(tree_size - 1)

def changeNum(i, num):
    i = i
    tree[i] = num
    i = i // 2
    while i > 0:
        tree[i] = (tree[2 * i] * tree[2 * i + 1]) % MOD
        i = i // 2

def getMul(start, end):
    temp = 1
    while start <= end:
        if start % 2 == 1:
            temp = (temp * tree[start]) % MOD
            start += 1
        if end % 2 == 0:
            temp = (temp * tree[end]) % MOD
            end -= 1
        start = start // 2
        end = end // 2
    print(temp)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        changeNum(b + start_index - 1, c)
    elif a == 2:
        getMul(b + start_index - 1, c + start_index - 1)
