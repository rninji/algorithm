import sys
import heapq

# 입력
N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 풀이
rooms = [0]
time.sort()
for t in time:
    if rooms[0] <= t[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, t[1])
    
# 출력
print(len(rooms))