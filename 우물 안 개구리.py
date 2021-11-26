import sys

N, M = map(int, sys.stdin.readline().split())
W = list(map(int, sys.stdin.readline().split()))
isBest = [True] * N
cnt = 0

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())

    if W[A-1] > W[B-1]: # B회원이 A보다 못 드므로 B회원은 최고라 생각하지 않는다 
        isBest[B-1] = False

    elif W[A-1] < W[B-1]: # A회원이 B보다 못 드므로 A회원은 최고라 생각하지 않는다
        isBest[A-1] = False

    else: # A회원 B회원이 드는 무게가 같으므로 서로 최고라 생각하지 않는다
        isBest[A-1] = False
        isBest[B-1] = False
    
for member in isBest: # isBest에서 True인 회원은 자신이 최고라고 생각하는 회원
    if member == True:
        cnt += 1

print(cnt)