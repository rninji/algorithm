import sys
import heapq
INF = float('inf')

# 입력
N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, sys.stdin.readline().split())



# 풀이
def dijk(start, next):
    cost = [INF] * (N+1)
    que = []
    heapq.heappush(que, [0, start])
    cost[start] = 0

    while que:
        now_w, now_node = heapq.heappop(que)
        for next_node, w in graph[now_node]:
            next_w = now_w + w
            if next_w >= cost[next_node]:
                continue
            cost[next_node] = next_w
            heapq.heappush(que, [next_w, next_node])
    return cost[1], cost[next], cost[N]
    

v1To1, v1ToV2, v1ToN = dijk(v1, v2) # v1에서의 (1, v2, N) 최단거리
v2To1, v2ToV1, v2ToN = dijk(v2, v1) # v2에서의 (1, v1, N) 최단거리

# 출력
dis = min((v1To1 + v1ToV2 + v2ToN),(v2To1 + v1ToV2 + v1ToN))
print(dis if dis!=INF else -1)