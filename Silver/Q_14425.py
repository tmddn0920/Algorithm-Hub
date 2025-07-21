result = 0

class Node(object):
    def __init__(self, end_node):
        self.end_node = end_node
        self.child_node = {}
        
class Tree(object):
    def __init__(self):
        self.parent = Node(None)
        
    def add_node(self, string):
        temp = self.parent
        length = 0
        for word in string:
            if word not in temp.child_node:
                temp.child_node[word] = Node(word)
            temp = temp.child_node[word]
            length += 1
            if length == len(string):
                temp.end_node = True
                
    def search_node(self, string):
        global result
        length = 0
        temp = self.parent
        for word in string:
            if word in temp.child_node:
                temp = temp.child_node[word]
                length += 1
                if length == len(string) and temp.end_node == True:
                    result += 1
        
N, M = map(int, input().split())
Tree = Tree()

for _ in range(N):
    word = input().strip()
    Tree.add_node(word)
    
for _ in range(M):
    word = input().strip()
    Tree.search_node(word)
    
print(result)