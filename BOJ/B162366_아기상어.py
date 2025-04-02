di = [0,0,1,-1]
dj = [1,-1,0,0]

# 입력
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 풀이
time = 0
weight = 2
ate = 0
si, sj = 0, 0

# 시작 위치 탐색
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            si, sj = i, j

def bfs(si, sj):
    eat_fish = [N, N, float("inf")] # 먹을 물고기 위치 (i,j), 거리
    
    que = []
    visit = [[False] * N for _ in range(N)]
    que.append([si, sj, 0])
    visit[si][sj] = True
    
    while(que):
        i, j, r = que.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or nj < 0 or ni >= N or nj >= N or visit[ni][nj] or weight < board[ni][nj]:
                continue
            que.append([ni,nj, r+1])
            visit[ni][nj] = True
            next_weight = board[ni][nj]
            if next_weight != 0 and next_weight < weight:
                if (eat_fish[2] > r+1) or (eat_fish[2] == r+1 and (eat_fish[0] > ni or (eat_fish[0] == ni and eat_fish[1] > nj))): 
                    eat_fish = [ni, nj, r+1]
    return eat_fish

while(True):
    # 먹을 수 있는 물고기 체크
    fish = bfs(si, sj)

    # 없으면 종료
    if (fish[2]==float("inf")):
        break

    # 이동 후 물고기 먹기
    board[si][sj] = 0
    si, sj = fish[0], fish[1]
    board[si][sj] = 9
    
    # 몸무게 증량
    ate += 1
    if weight <= ate:
        weight += 1
        ate = 0
        
    # 시간 증가
    time += fish[2]

# 출력
print(time)