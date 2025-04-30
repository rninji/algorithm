import sys

# 입력
N, M, K = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 풀이

# 이동 방향 (동 남 서 북)
dir = 0
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

# 다이스 위치
pos = [0, 0]

# 점수
score = 0

# (x, y)에 대한 점수 구하기
def BFS(x, y):
    score = board[x][y]
    cnt = 0
    visit = [[False] * M for _ in range(N)]
    que = [[x, y]]
    visit[x][y] = True
    while que:
        cnt += 1
        i, j = que.pop(0)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if ni<0 or nj<0 or ni>=N or nj>=M or visit[ni][nj] or board[ni][nj]!=score:
                continue
            que.append([ni, nj])
            visit[ni][nj] = True
    return score * cnt

# 전개도
dice = [[0,2,0],
       [4,1,3],
       [0,5,0],
        [0,6,0]]

# 회전
def left(d1, d2, d3, d4):
    return d2, d3, d4, d1
    
def right(d1, d2, d3, d4):
    return d4, d1, d2, d3

def rot(dir):
    if dir == 0: #동
        dice[1][1], dice[1][2], dice[3][1], dice[1][0] = right(dice[1][1], dice[1][2], dice[3][1], dice[1][0])
    elif dir == 1: # 남
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = right(dice[0][1], dice[1][1], dice[2][1], dice[3][1])
    elif dir == 2: #서
        dice[1][1], dice[1][2], dice[3][1], dice[1][0] = left(dice[1][1], dice[1][2], dice[3][1], dice[1][0])
    else: # 북
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = left(dice[0][1], dice[1][1], dice[2][1], dice[3][1])

# main
for i in range(K):
    # 주사위 이동 
    pos[0] += di[dir]
    pos[1] += dj[dir]
    if pos[0] < 0 or pos[1] < 0 or pos[0] >= N or pos[1] >= M:
        dir = (dir+2)%4
        pos[0] += 2 * di[dir]
        pos[1] += 2 * dj[dir]
    # 해당 칸 BFS로 점수 추가
    score += BFS(pos[0], pos[1])
    # 주사위 전개도 변화
    rot(dir)
    # 이동방향 결정
    if dice[3][1] > board[pos[0]][pos[1]]:
        dir = (dir+1)%4
    elif dice[3][1] < board[pos[0]][pos[1]]:
        dir = (dir+3)%4
    
# 출력
print(score)