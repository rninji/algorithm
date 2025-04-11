import sys
sys.setrecursionlimit(100000)
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j, baechu, visit, M, N):
    visit[i][j] = True
    for k in range(4):
        ni = i+di[k]
        nj = j+dj[k]
        if ni<0 or nj<0 or ni>=N or nj>=M or not baechu[ni][nj] or visit[ni][nj]:
            continue
        visit = dfs(ni, nj, baechu, visit, M, N)
    return visit

# 입력
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    baechu = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        baechu[y][x] = 1

    # 풀이
    answer = 0
    visit = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not baechu[i][j] or visit[i][j]:
                continue
            answer += 1
            visit = dfs(i, j, baechu, visit, M, N)
            
    # 출력
    print(answer)