import sys

K, P, N = map(int, sys.stdin.readline().split())

# pow() 계산시 mod값 설정을 하여 시간단축을 시킨 후 K를 곱한 값이 1e9+7 을 넘어갈 수 있기 때문에 한번더 1e9+7로 나눈 나머지 값을 구한다
print(K*pow(P,N, int(1e9+7)) % int(1e9+7))