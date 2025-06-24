import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

def isPrime(num):
    for n in range(2, int((num / 2) + 1)):
        if num % n == 0:
            return False
    return True

def dfs(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                dfs(number * 10 + i)

dfs(2)
dfs(3)
dfs(5)
dfs(7)