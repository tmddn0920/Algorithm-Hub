import sys
input = sys.stdin.readline

id_pw = {}
n, m = map(int, input().split())
for num in range(n):
    line = input().split()
    id_pw[line[0]] = line[1]
for num in range(m):
    line = input().strip()
    if line in id_pw.keys():
        print(id_pw[line])