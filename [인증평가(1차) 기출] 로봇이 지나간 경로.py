import sys
from collections import deque

def bfs():
    queue = deque()
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < H and 0 <= ny < W:
                pass

H, W = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
directions = ['<','>','v','^']

for row in range(H):
    if maps[row].count('#') % 2 == 1 and maps[row].count('#') >= 3:
        
        for col in range(W):
            if maps[row][col] == '#':
                cnt = 0
                
                for i in range(4):
                    nx = row + dx[i]
                    ny = col + dy[i]
                    
                    if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == '#':
                        direction = directions[i]
                        cnt += 1
                
                if cnt == 1:
                    bfs()
                        