import sys
from collections import deque

def bfs(x,y):
    global cnt 

    dx = [-1,1,0,0] # x축 방향 설정
    dy = [0,0,-1,1] # y축 방향 설정
    queue = deque([[x,y]]) # 처음 시작점
    
    while queue:
        x, y = queue.popleft() 
        for i in range(4): # 상하좌우 탐색
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if map[nx][ny] == '1': 
                    map[nx][ny] = '0' # '1'인 좌표를 발견하면 카운트 해주고 다시 탐색되지 않도록 0으로 바꿔줌
                    queue.append([nx,ny]) # 상하좌우 탐색 시 '1'인 곳을 발견하면 좌표를 queue에 넣어줘서 그 좌표에서 다시 탐색하도록 만듬
                    cnt += 1


N = int(sys.stdin.readline())
map = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = []

for i in range(N):
    for j in range(N):
        if map[i][j] == '1':
            map[i][j] = 0
            cnt = 1
            bfs(i,j) # '1'인 곳을 발견하면 bfs문 실행
            answer.append(cnt)

answer.sort() # 오름차순으로 정렬
print(len(answer))
print(*answer, sep="\n") # unpacking과 sep을 이용해 한줄로 출력코드 표현