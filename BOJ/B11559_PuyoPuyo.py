import copy
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 입력
field = []
for i in range(12):
  field.append(list(input()))


# BFS
def BFS(i, j, visit):
  queue = []
  queue.append([i,j])
  visit[i][j] = True
  cnt = 1
  fieldCopy[i][j] = '.'
  while(queue):
    now = queue.pop(0)
    # 사방탐색
    for k in range(4):
      ni = now[0] + di[k]
      nj = now[1] + dj[k]
      if ni<0 or nj<0 or ni>=12 or nj>=6 or visit[ni][nj] or field[i][j]!=field[ni][nj]:
        continue
      queue.append([ni,nj])
      visit[ni][nj] = True
      cnt += 1
      fieldCopy[ni][nj] = '.'
  return cnt

# 풀이
answer = 0
boom = True
while(boom): # 더이상 터지지 않을 때까지
  boom = False
  visit = [[False for _ in range(6)] for _ in range(12)]

  # 뿌요 만날 때마다 인접 뿌요 확인해서 4개 이상이면 터뜨리기
  for i in range(12):
    for j in range(6):
      if field[i][j] == '.' or visit[i][j]:
        continue
      fieldCopy = copy.deepcopy(field)
      cnt = BFS(i, j, visit)
      if cnt >= 4:
        boom = True
        field = copy.deepcopy(fieldCopy)
        
  if boom: # 1번 이상 터졌으면 내리기
    answer += 1
    for j in range(5, -1, -1):
      down = 12
      prev = ''
      i = 12
      while(i>0):
        i -= 1
        if field[i][j] == '.' and prev!='.':
          down = i
        elif field[i][j] != '.' and down >= 0 and down < 12:
          field[down][j] = field[i][j]
          field[i][j] = '.'
          i = down
          down -= 1
        prev = field[i][j]
        
# 출력
print(answer)