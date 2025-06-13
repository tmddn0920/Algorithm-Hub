from queue import PriorityQueue
import sys
input = sys.stdin.readline

num = int(input())
myQueue = PriorityQueue()
for _ in range(num):
    request = int(input())
    if request == 0:
        if myQueue.empty():
            print(0)
        else:
            temp = myQueue.get()
            print(temp[1])
    else:
        myQueue.put((abs(request), request))