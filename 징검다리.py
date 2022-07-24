import sys

N = int(sys.stdin.readline())
stone_height = list(map(int, sys.stdin.readline().split()))

# Dynamic Programming 이용
dp = [1] * N

for i in range(1,N):
    for j in range(i):
        if stone_height[i] > stone_height[j]: # 현재보다 높은 돌을 밟아야 하므로
            dp[i] = max(dp[i], dp[j]+1) # 가장 많이 돌을 밟는 경우의 수를 구함

print(max(dp))