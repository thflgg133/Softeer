import sys

N, K = map(int, sys.stdin.readline().split())
PH_line = list(sys.stdin.readline().rstrip())
cnt = 0

for i in range(N):
    if PH_line[i] == "P":  # 로봇일 경우에만 작동
        for j in range(-K+i,K+i+1): # 로봇이 부품을 집을 수 있는 범위 안에서 왼쪽 부터 차례대로 탐색
            if j < 0 or j > N-1: # 범위를 벗어나면 IndexError가 뜨기 때문에 지나감
                continue
            
            # 부품을 집을경우 집었다는 처리를 하고 카운트를 센 후 다음 로봇으로 넘어간다
            elif PH_line[j] == "H": 
                PH_line[j] = None 
                cnt += 1
                break
 
print(cnt)