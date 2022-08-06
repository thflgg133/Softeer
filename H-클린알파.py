import sys

P, N = map(int, sys.stdin.readline().split())
virus = list(map(int, sys.stdin.readline().split()))

ans = 0 
mod = 1000000007

for i in range(N-2, -1, -1):
    # pow 함수를 이용해 효율적인 나머지 연산
    virus[i] *= pow(P, (N-i-1), mod)

print(sum(virus) % mod)