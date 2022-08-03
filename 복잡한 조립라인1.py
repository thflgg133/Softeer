import sys

K, N = map(int, sys.stdin.readline().split())

dp = []
travel_time = [[[0 for i in range(K)] for j in range(K)] for k in range(N)]

for i in range(N-1):
    line = list(map(int, sys.stdin.readline().split()))
    dp.append(line[:K]) # 작업 시간
    cnt = 0

    for j in range(K):
        for k in range(K):
            if j == k:
                continue

            # 각 작업장 사이를 이동하는 시간들을 전부 할당
            travel_time[i][j][k] = line[K + cnt]
            cnt += 1

# 마지막 라인에는 이동시간이 없으므로 따로 추가   
dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(N-1):
    for j in range(K):
        tmp = dp[i][j]
        for k in range(K):
            if j == k: # 같은 번호의 작업장으로 이동할 때는 이동 시간이 안걸리므로 패스
                continue
            
            # min(같은 번호의 작업장으로 이동, 다른 번호의 작업장으로 이동하는 시간 + 작업 시간)
            # 19번째 줄과 다르게 j,k를 반대로 넣어줘야 함
            tmp = min(tmp, dp[i][k] + travel_time[i][k][j]) 
        
        dp[i+1][j] += tmp

print(min(dp[-1]))