di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

# 입력
N = int(input())
m = []
for _ in  range(N):
     m.append(list(map(int,input())))

# 풀이
total = 0
counts = []
visit = [[False for i in range(N)] for j in range(N)]

# BFS
def count(si, sj):
    global visit
    cnt = 1
    que = []
    que.append([si, sj])
    visit[si][sj] = True
    while(que):
        i, j = que.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni<0 or nj<0 or ni>=N or nj>=N or m[ni][nj]==0 or visit[ni][nj]:
                continue
            que.append([ni, nj])
            visit[ni][nj] = True
            cnt += 1
    return cnt
    

for i in range(N):
    for j in range(N):
        if m[i][j] == 1 and not visit[i][j]:
            total += 1
            counts.append(count(i, j))

# 출력
print(total)
counts.sort()
for c in counts:
    print(c)