import sys
from collections import deque

def bfs():
    queue = deque([[0,0]])  # 얼음의 가장자리 지점은 얼음이 존재하지 않으므로 0,0 부터 시작
    visited[0][0] = 1

    while queue:
        y, x = queue.popleft()
        
        for i in range(4): # 현재위치에서 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M: 
                if ice_land[ny][nx]: #  탐색하는 곳이 얼음이라면
                    visited[ny][nx] += 1 # 방문횟수 1 증가

                elif visited[ny][nx] == 0: # 탐색하는 곳이 얼음이 아니라면
                    queue.append([ny,nx]) # 그 지점도 탐색을 해야하므로 queue에 다시 넣어준다
                    visited[ny][nx] = 1 # 방문횟수를 1로 초기화

    for y in range(N):
        for x in range(M):
            if visited[y][x] >= 2: #  방문횟수가 2이상인 곳은 얼음이 2번이상 외부 공기와 접촉한 곳이므로 녹음
                ice_land[y][x] = 0


N, M = map(int, sys.stdin.readline().split())
ice_land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 상하좌우 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

while True: # ice_land 안에 얼음이 존재하지 않을 때 까지 시도
    if ice_land.count([0] * M) == N: 
        break

    visited = [[0] * M for _ in range(N)] # bfs()가 시도되기 전에 계속 방문 횟수를 계속 초기화 해줘야 한다
    bfs()
    cnt += 1
        
print(cnt)