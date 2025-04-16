import sys
import heapq

# 입력
N, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(D+1)]
for i in range(N):
    s, f, d = map(int, sys.stdin.readline().split())
    if f-s > d and f <= D: 
        graph[s].append([f, d])

# 풀이
for i in range(D): # 고속도로 정보 추가
    graph[i].append([i+1, 1])

dis = [float('INF') for _ in range(D+1)]
dis[0] = 0
heap = []
heapq.heappush(heap, [0, 0])

while heap:
    nowd, now = heapq.heappop(heap)
    if dis[now] < nowd:
        continue
    for g in graph[now]:
        if dis[g[0]] > nowd + g[1]:
            dis[g[0]] = nowd + g[1]
            heapq.heappush(heap,[nowd + g[1], g[0]])

# 출력
print(dis[D])