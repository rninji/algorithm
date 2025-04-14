import sys

# 입력
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
fin = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            fin = [i, j]

# 풀이
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
visit = [[False] * m for _ in range(n)]
que = [[fin[0], fin[1], 0]]
board[fin[0]][fin[1]] = 0
visit[fin[0]][fin[1]] = True
while que:
    i, j, d = que.pop(0)
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if ni<0 or nj<0 or ni>=n or nj>=m or board[ni][nj] == 0 or visit[ni][nj]:
            continue
        que.append([ni, nj, d+1])
        board[ni][nj] = d+1
        visit[ni][nj] = True

# 출력
for i in range(n):
    for j in range(m):
        print(-1 if board[i][j] and not visit[i][j] else board[i][j], end=' ')
    print()
