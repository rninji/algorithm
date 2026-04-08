N = int(input())
a = [list(input()) for _ in range(N)]

# 심장
def find_heart():
    for i in range(N):
        for j in range(N):
            if a[i][j] == '*':
                return i+1, j
                
heart = []
heart = find_heart()

# 왼쪽 팔
ran = []
tmp = 0
for i in range(heart[1]-1, -2, -1):
    if i <= -1 or a[heart[0]][i] != '*':
        ran.append(tmp)
        break;
    tmp += 1

# 오른쪽 팔
tmp = 0
for i in range(heart[1]+1, N+1):
    if i>= N or a[heart[0]][i] != '*':
        ran.append(tmp)
        break;
    tmp += 1

# 허리
tmp = 0
leg_start = 0
for i in range(heart[0]+1, N):
    if a[i][heart[1]] != '*':
        ran.append(tmp)
        leg_start = i
        break;
    tmp += 1

# 왼쪽 다리
tmp = 0
for i in range(leg_start, N+1):
    if i>=N or a[i][heart[1]-1] != '*':
        ran.append(tmp)
        break;
    tmp += 1
    
# 오른쪽 다리
tmp = 0
for i in range(leg_start, N+1):
    if i>=N or a[i][heart[1]+1] != '*':
        ran.append(tmp)
        break;
    tmp += 1

# 출력
print(heart[0]+1, heart[1]+1)
for i in range(5):
    print(ran[i], end = ' ')
