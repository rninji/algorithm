import sys

# 입력
N, L, R = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 풀이
visit = []
di = [0,0,1,-1]
dj = [1,-1,0,0]

# 연합 확인
def check(i, j):
    que = [(i, j)] # 위치
    visit[i][j] = True
    guild = [[i,j]] # 연합
    cnt = A[i][j] # 누적인구수
    
    while que:
        now = que.pop(0)
        for k in range(4):
            ni, nj = now[0]+di[k], now[1]+dj[k]
            if ni<0 or nj<0 or ni>=N or nj>=N or visit[ni][nj]:
                continue
            if L <= abs(A[now[0]][now[1]] - A[ni][nj]) <= R:
                cnt += A[ni][nj]
                guild.append([ni, nj])
                visit[ni][nj] = True
                que.append([ni, nj])
    return guild, cnt

# 인구 이동
def move(guild, cnt):
    num = cnt//len(guild)
    for i, j in guild:
        A[i][j] = num

day = 0
while True:
    is_moved = False
    visit = [[False] * N for _ in range(N)]
    move_list = []

    # 연합 확인
    for i in range(N):
        for j in range(N):
            if visit[i][j]: 
                continue
            guild, cnt = check(i, j)
            if len(guild) > 1:
                move_list.append([guild, cnt])
    # 인구 이동
    for g, c in move_list:
        is_moved = True
        move(g, c)
                
    if not is_moved:
        break
    # 날짜 증가
    day += 1

# 출력
print(day)