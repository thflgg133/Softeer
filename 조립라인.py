import sys

N = int(sys.stdin.readline())
assembly_line = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

# Dynamic Programiing 활용
dp = [[0,0]] * N
dp[0] = [assembly_line[0][0], assembly_line[0][1]]

for i in range(1, N):
    dp[i] = [min(dp[i-1][0], dp[i-1][1] + assembly_line[i-1][3]) + assembly_line[i][0], # A 조립라인
             min(dp[i-1][1], dp[i-1][0] + assembly_line[i-1][2]) + assembly_line[i][1]] # B 조립라인

print(min(dp[N-1])) # A, B 조립라인 중 더 최소시간을 출력