import sys
import heapq

N = int(sys.stdin.readline())
meeting_time = []

for _ in range(N):
    start, end = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(meeting_time, (end, start))

end_time = 0
cnt = 0

while meeting_time:
    if meeting_time[0][1] >= end_time:
        end_time = heapq.heappop(meeting_time)[0]
        cnt += 1
        continue

    heapq.heappop(meeting_time)

print(cnt)