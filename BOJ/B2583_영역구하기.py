import sys
# 입력
M, N, K = map(int, sys.stdin.readline().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] = 1

# 풀이
answer = []
visit = [[False] * N for _ in range(M)]
di, dj = [0,0,1,-1], [1,-1,0,0]

def BFS(si, sj):
    cnt = 1
    que = [[si,sj]]
    visit[si][sj] = True
    while que:
        i, j = que.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j +dj[k]
            if ni<0 or nj<0 or ni>=M or nj>=N or visit[ni][nj] or board[ni][nj]:
                continue
            que.append([ni,nj])
            visit[ni][nj] = True
            cnt+=1
    return cnt

for i in range(M):
    for j in range(N):
        if board[i][j] or visit[i][j]:
            continue
        answer.append(BFS(i,j))

# 출력
print(len(answer))
print(*sorted(answer))