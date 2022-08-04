import sys

K, N = map(int, sys.stdin.readline().split())

dp = []
travel_time = []

for i in range(N-1):
    line = list(map(int, sys.stdin.readline().split()))
    dp.append(line[:K]) # 작업 시간
    travel_time.append(line[-1])

# 마지막 라인에는 이동시간이 없으므로 따로 추가   
dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(N-1):
    # 이동시간이 전부 같으므로 계속 최소시간이 걸리는 작업장을 찾아서 진행한다
    tmp = min(dp[i]) 

    for j in range(K):
        if i == j:
            dp[i+1][j] += dp[i][j]

        else:
            dp[i+1][j] += min(dp[i][j], tmp + travel_time[i])

print(min(dp[-1])) 