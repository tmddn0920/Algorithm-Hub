from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    clothes = defaultdict(list)
    
    for _ in range(n):
        name, category = input().split()
        clothes[category].append(name)
    
    result = 1
    for category in clothes:
        result *= len(clothes[category]) + 1 
    
    print(result - 1)  
