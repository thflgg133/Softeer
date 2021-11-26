import sys
from itertools import permutations

def UpandDown(rail): 
    total = 0
    cnt = 0 # 첫번째 레일부터 탐색하기 위해 선언

    for i in range(K):
        basket = 0

        while True:
            basket += rail[cnt]
            cnt = (cnt+1) % N # 마지막레일에 다다르면 다시 첫번째 레일부터 탐색 
            if basket + rail[cnt] > M: # 다음 레일에 있는 택배를 담았을때 바구니 무게를 초과하면 break
                break
            
        total += basket 

    return total  # K번 횟수를 실행해서 쌓인 total 값 반환 

N, M, K = map(int, sys.stdin.readline().split())
w = list(map(int, sys.stdin.readline().split()))

rail_arr = list(permutations(w, N))
answer = []

for rail in rail_arr:
    answer.append(UpandDown(rail))
    
print(min(answer))