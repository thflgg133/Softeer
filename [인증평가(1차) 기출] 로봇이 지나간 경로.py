import sys
from collections import deque

def check(x, y):
    cnt = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < H and 0 <= ny < W and maps[nx][ny] == '#':
            start = directions[i]
            cnt += 1

    if cnt > 1:
        return False

    return start


def bfs(i, j):
    queue = deque([[i,j]])
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            direction = directions[i]
            
            if 0 <= nx < H and 0 <= ny < W:
                if maps[nx][ny] == '#' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    arr.append(direction)
                    queue.append([nx,ny])
                    

    return arr

H, W = map(int, sys.stdin.readline().split())
maps = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
visited = [[False] * W for _ in range(H)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
directions = ['^','>','v','<']
ans = []

for row in range(H):       
    for col in range(W):
        if maps[row][col] == '#' and check(row, col):
            arr = deque([])
            path = bfs(row, col)
            print(*path)
            sys.exit(0)