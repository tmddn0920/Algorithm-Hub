import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    max_hq = []
    min_hq = []
    isValid = defaultdict(int)
    K = int(input())
    for _ in range(K):
        A, B = map(str, input().split())
        num = int(B)
        if A == 'I':
            heapq.heappush(max_hq, -num)
            heapq.heappush(min_hq, num)
            isValid[num] += 1
        elif A == 'D':
            if num == 1:
                while max_hq:
                    x = -heapq.heappop(max_hq)
                    if isValid[x] > 0:
                        isValid[x] -= 1
                        break
            elif num == -1:
                while min_hq:
                    x = heapq.heappop(min_hq)
                    if isValid[x] > 0:
                        isValid[x] -= 1
                        break
    while min_hq and isValid[min_hq[0]] == 0:
        heapq.heappop(min_hq)
    while max_hq and isValid[-max_hq[0]] == 0:
        heapq.heappop(max_hq)
              
    if not min_hq or not max_hq:
        print('EMPTY')
    else:
        print(-max_hq[0], min_hq[0])