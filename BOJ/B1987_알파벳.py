import sys
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]

# 입력
R, C = map(int, sys.stdin.readline().split())
words = [list(sys.stdin.readline().strip()) for _ in range(R)]

# 풀이
result = 0
check = [False] * 26
def dfs(i, j, count):
    global result
    count+=1
    result = max(result, count)
    for k in range(4):
        ni, nj = i+di[k], j+dj[k]
        if ni<0 or nj<0 or ni>=R or nj>=C or check[ord(words[ni][nj])-65]:
            continue
        check[ord(words[ni][nj])-65] = True
        dfs(ni, nj, count)
        check[ord(words[ni][nj])-65] = False

check[ord(words[0][0])-65] = True
dfs(0,0,0)

# 출력
print(result)