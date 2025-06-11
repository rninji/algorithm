import sys

# 입력
N, M, x, y, K = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move = list(map(int, sys.stdin.readline().split()))

# x, 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

dice = [0, 0, 0, 0, 0, 0] # 위, 북, 동, 서, 남, 아래

def change(n1, n2, n3, n4):
    return n4, n1, n2, n3

def roll(dir):
    if dir == 1: # 동
        dice[3], dice[0], dice[2], dice[5] = change(dice[3], dice[0], dice[2], dice[5])
    elif dir == 2: # 서
        dice[5], dice[2], dice[0], dice[3] = change(dice[5], dice[2], dice[0], dice[3])
    elif dir == 3: # 북
        dice[0], dice[1], dice[5], dice[4] = change(dice[0], dice[1], dice[5], dice[4])
    elif dir == 4: # 남
        dice[4], dice[5], dice[1], dice[0] = change(dice[4], dice[5], dice[1], dice[0])
    
for m in move:
    # 이동
    x += dx[m]
    y += dy[m]
    if (x<0 or x>=N or y<0 or y>=M): # 범위 밖이면 무시
        x -= dx[m]
        y -= dy[m]
        continue;

    # 주사위 굴리기
    roll(m)

    # 바닥면 복사
    if nums[x][y] == 0:
        nums[x][y] = dice[5]
    else:
        dice[5] = nums[x][y]
        nums[x][y] = 0
        
    # 윗면 출력
    print(dice[0])