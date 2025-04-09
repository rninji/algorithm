import sys
import heapq

# 입력
N =  int(sys.stdin.readline())
M =  int(sys.stdin.readline())
bus = [[] for _ in range(N+1)]
for _ in range(M):
    arr, dep, cost = map(int, sys.stdin.readline().split())
    bus[arr].append([dep, cost])
arr, dep = map(int, sys.stdin.readline().split())

INF = float('inf')


# 풀이
def dijk(arr, dep):
    cost = [INF for _ in range (N+1)]
    que = []

    cost[arr] = 0
    heapq.heappush(que, [0, arr])

    while que:
        now_c, now_city = heapq.heappop(que)
        if now_c > cost[now_city]:
            continue
        for next_city, c in bus[now_city]:
            next_c = now_c + c
            if next_c >= cost[next_city]:
                continue
            cost[next_city] = next_c
            heapq.heappush(que, [next_c,  next_city])
    return cost[dep]

# 출력
print(dijk(arr, dep))
    