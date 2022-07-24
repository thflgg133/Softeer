import sys
import bisect # 이분 탐색

N = int(sys.stdin.readline())
stone_height = list(map(int, sys.stdin.readline().split()))

dp_front = [stone_height[0]] # 앞 쪽 기준 밟을 수 있는 돌의 유효한 오름차순 높이
dp_back = [stone_height[-1]] # 뒷 쪽 기준 밟을 수 있는 돌의 유효한 오름차순 높이
front_cnt = [1] * N # 앞에서 부터 밟은 돌의 갯수
back_cnt = [1] * N # 뒤에서 부터 밟은 돌의 갯수

# 앞 쪽 기준
for i in range(N):
    if stone_height[i] > dp_front[-1]:
        dp_front.append(stone_height[i])

    else:
        # 이분탐색을 이용하여 logN의 복잡도로 이전의 가장 큰 원소의 idx값을 찾는다.
        idx = bisect.bisect_left(dp_front, stone_height[i])
        dp_front[idx] = stone_height[i]

    front_cnt[i] = len(dp_front)

# 뒷 쪽 기준
stone_height.reverse()

for i in range(N):
    if stone_height[i] > dp_back[-1]:
        dp_back.append(stone_height[i])

    else:
        # 이분탐색을 이용하여 logN의 복잡도로 이전의 가장 큰 원소의 idx값을 찾는다.
        idx = bisect.bisect_left(dp_back, stone_height[i])
        dp_back[idx] = stone_height[i]
        
    back_cnt[N-i-1] = len(dp_back)

ans = 0
for i in range(N):
    ans = max(ans, front_cnt[i] + back_cnt[i])

print(ans-1) # 가장 높은 크기의 돌이 2번 밟히기 때문에 -1 을 한다.