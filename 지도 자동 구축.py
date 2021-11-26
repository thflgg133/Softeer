import sys

N = int(sys.stdin.readline())
dp = [0] * 16 # N의 최댓값은 15이기 때문에 0단계 ~ 15단계 총 16개 칸 생성
dp[0] = 2 # Start 지점의 한변의 점의 개수 = 2

# N번째 단계의 한 변의 점의 개수는 (N-1번째 점의 개수 + N-1번째 점의 개수-1) 과 같다
for i in range(1,N+1):
    dp[i] = dp[i-1] + (dp[i-1] -1) 

# print(dp) -> 각 단계에서 한 변의 점의 개수
print(dp[N]**2) # 총 점의 개수 = 한 변의 점 개수의 제곱