import sys
input = sys.stdin.readline

not_listen = set()
n, m = map(int, input().split())

for i in range(n):
    name = input().strip()
    not_listen.add(name)
    
result_arr = []
for i in range(m):
    name = input().strip()
    if name in not_listen:
        result_arr.append(name)
        
result_arr.sort()
print(len(result_arr))
for i in result_arr:
    print(i)