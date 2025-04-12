import sys

# 입력
N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

# 0: 빈칸, 1: 사과, 2: 꼬리 시계 반대방향회전, 4: 꼬리 시계방향 회전, 9: 뱀
board = [[0] * (N+1) for _ in range(N+1)] 

for _ in range(K):
    i, j = map(int, sys.stdin.readline().split())
    board[i][j] = 1
    
L = int(sys.stdin.readline())
turn = []
for _ in range(L):
    x, c = sys.stdin.readline().split()
    turn.append([int(x), -1 if c=='L' else 1])

# 풀이
# 오른쪽, 아래, 왼쪽, 위
ti = [0, 1, 0, -1]
tj = [1, 0, -1, 0]

head = [1, 1, 0] # 머리 위치, 방향
snake = [[1,1]] # 뱀 위치
time = 0 # 시간
board[1][1] = 9

while(True):
    time+=1
    
    # 몸길이 늘려 머리를 다음칸에 위치
    ni, nj = head[0]+ti[head[2]], head[1]+tj[head[2]]
    head = [ni,nj,head[2]]
    snake.append([ni, nj])
    
    # 벽이나 자신에게 부딪히면 게임 종료
    if ni<=0 or nj<=0 or ni>N or nj>N or board[ni][nj]==9:
        break
    
    # 사과가 있다면 사과 없어지고 꼬리 움직이지 않음
    elif board[ni][nj]==1:
        board[ni][nj]=0
        
    # 사과 없다면 꼬리 비워줌
    else:
        t1, t2 = snake.pop(0)
        board[t1][t2] = 0
    board[ni][nj]=9

    # 시간되면 뱀 방향 전환
    if turn and turn[0][0]<=time:
        head[2] = (head[2]+turn.pop(0)[1]+4)%4
        
# 출력
print(time)
    