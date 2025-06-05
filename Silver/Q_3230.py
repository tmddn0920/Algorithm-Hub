N, M = map(int, input().split())
round_one = []
round_two = []

for n in range(1, N + 1):
    current_ranking = int(input())
    round_one.insert(current_ranking - 1, n)
    
for m in reversed(round_one[:M:]):
    current_ranking = int(input())
    round_two.insert(current_ranking - 1, m)
    
print(*round_two[:3], sep='\n')