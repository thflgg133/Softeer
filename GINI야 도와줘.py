import sys
from collections import deque

def shower(): # 소나기 이동
    global rain
    tmp = [] 
    for x, y in rain:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                if map[nx][ny] == ".":
                    map[nx][ny] = "*"
                    tmp.append((nx,ny))

    rain = list(set(rain+tmp)) # 소나기가 전파된 위치 추가, set을 이용해 중복되는 좌표는 제거
    return


def bfs(x,y):
    tmp = 0
    visit[x][y] = True
    queue = deque([[x,y,0]])
    shower() # 처음은 if문이 실행되지 않으므로 임의로 shower()문이 실행되게 해줌

    while queue:
        x, y, cnt= queue.popleft() # 세차장의 위치에서 시작
        if tmp != cnt: # 시간이 증가 할때만 소나기가 확산되도록 만듬 
            shower()

        tmp = cnt 
      
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < R and 0 <= ny < C:
                if map[nx][ny] == 'H': # 집에 도달하면 종료
                    return cnt+1
                
                if map[nx][ny] == "." and visit[nx][ny] == False: # 비어있는 칸이고 방문하지 않은 곳 일때
                    visit[nx][ny] = True # 방문처리
                    queue.append([nx,ny,cnt+1]) # 이동한 좌표, 이동횟수 
    return "FAIL" # queue가 빌때까지 집에 도달하지 못하면 FAIL

                    
R, C = map(int, sys.stdin.readline().split())
map = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

visit = [[False] * C for _ in range(R)]
position = [] # 세차장 위치
rain = [] # 소나기 좌표들

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(R):
    for j in range(C):
        if map[i][j] == 'W':
            position.append((i,j)) # 현재 위치 파악
            
        if map[i][j] == '*':
            rain.append((i,j)) # 소나기가 있는 위치들 파악

print(bfs(position[0][0], position[0][1]))