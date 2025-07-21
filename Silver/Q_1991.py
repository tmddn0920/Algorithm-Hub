N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]
    
def foward(node):
    if node == '.':
        return
    print(node, end = "")
    foward(tree[node][0])
    foward(tree[node][1])
 
def middle(node):
    if node == '.':
        return
    middle(tree[node][0])
    print(node, end = "")
    middle(tree[node][1])
    
def backward(node):
    if node == '.':
        return
    backward(tree[node][0])
    backward(tree[node][1])
    print(node, end = "")
    
foward('A')
print()
middle('A')
print()
backward('A')