# 입력
wheel = [0]*4
for i in range(4):
    wheel[i] = list(map(int, str(input())))
K = int(input())
rot = []
for i in range(K):
    rot.append(list(map(int, input().split())))

# 풀이
def rotation(wnum, dir, come): # 톱니번호, 회전방향, 어디서왔는지(-1:왼쪽톱니, 0:자가회전, 1:오른쪽톱니)
    # 왼쪽 톱니바퀴 회전
    if wnum != 1 and come!=-1 and wheel[wnum-1][6]!=wheel[wnum-2][2]: 
        rotation(wnum-1, -dir, 1)
    # 오른쪽 톱니바퀴 회전
    if wnum != 4 and come!= 1 and wheel[wnum-1][2]!=wheel[wnum][6]:
        rotation(wnum+1, -dir, -1)
    # 회전
    if dir == 1: # 시계
        tmp = wheel[wnum-1][7]
        for i in range(7,-1,-1):
            wheel[wnum-1][i] = wheel[wnum-1][i-1]
        wheel[wnum-1][0] = tmp
    else: # 반시계
        tmp = wheel[wnum-1][0]
        for i in range(7):
            wheel[wnum-1][i] = wheel[wnum-1][i+1]
        wheel[wnum-1][7] = tmp

# 회전
for r in rot:
    rotation(r[0], r[1], 0)

# 출력
print(wheel[0][0] + wheel[1][0]*2 + wheel[2][0]*4 + wheel[3][0]*8)
