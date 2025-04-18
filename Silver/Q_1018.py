m, n = map(int, input().split())
chessboard = [input() for _ in range(m)]

def count_repaint(x, y):
    repaint_w = 0
    repaint_b = 0
    
    for i in range(8):
        for j in range(8):
            current = chessboard[x + i][y + j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
            
    return min(repaint_w, repaint_b)
    
min_count = 64

for i in range(m - 7):
    for j in range(n - 7):
        min_count = min(min_count, count_repaint(i, j))
        
print(min_count)
        
                    