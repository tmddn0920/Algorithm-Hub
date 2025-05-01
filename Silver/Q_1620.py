import sys
input = sys.stdin.readline

pokemon = {}
n, m = map(int, input().split())

for i in range(1, n + 1):
    name = input().strip()
    pokemon[i] = name

reverse_pokemon = {v: k for k, v in pokemon.items()}

for i in range(m):    
    problem = input().strip()
    if problem.isdigit():
        problem = int(problem)
        print(pokemon[problem])
    else:
        print(reverse_pokemon[problem])