# 입력
N, M, V = map(int, input().split())
graph = [[] for i in range(N+1) ]
for _ in range(M):
  i, j = map(int, input().split())
  graph[i].append(j)
  graph[j].append(i)

# 풀이
for i in graph:
  i.sort()

# DFS
def dfs(graph, visit, v):
  visit[v] = True
  print(v, end=' ')
  for next in graph[v]:
    if visit[next] == False:
      dfs(graph, visit, next)
      
visit = [False] * (N+1)
dfs(graph, visit, V)

# BFS
print()
queue = []
visit = [False] * (N+1)
queue.append(V)
visit[V] = True
while(queue):
  v = queue.pop(0)
  print(v, end=' ')
  for next in graph[v]:
    if visit[next] == False:
      queue.append(next)
      visit[next] = True
  