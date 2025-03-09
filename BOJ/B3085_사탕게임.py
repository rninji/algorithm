import copy

# 입력
N = int(input())
colors = []
for _ in range(N):
  colors.append(list(input()))

# 풀이
# 가장 긴 연속 사탕 세기
def countMax(colors):
  maxCnt = 0

  # 가로 세기
  for line in colors:
    cnt = 0
    prev = ''
    for color in line:
      if prev == color:
        cnt += 1
      else :
        cnt = 1
        prev = color
      maxCnt = max(cnt, maxCnt)

  # 세로 세기
  for j in range(N):
    cnt = 0
    prev = ''
    for i in range(N):
      if prev == colors[i][j]:
        cnt += 1
      else :
        cnt = 1
        prev = colors[i][j]
      maxCnt = max(cnt, maxCnt)
      
  return maxCnt


answer = 0

# 사탕 두 개 교환
for i in range(N):
  for j in range(N):
    if i != N-1: # 세로 교환
      if colors[i][j] != colors[i+1][j]:
        colorsCopy = copy.deepcopy(colors)
        colorsCopy[i][j], colorsCopy[i+1][j] = colorsCopy[i+1][j], colorsCopy[i][j]
        answer = max(answer, countMax(colorsCopy))
    if j != N-1: # 가로 교환
      if colors[i][j] != colors[i][j+1]:
        colorsCopy = copy.deepcopy(colors)
        colorsCopy[i][j], colorsCopy[i][j+1] = colorsCopy[i][j+1], colorsCopy[i][j]
        answer = max(answer, countMax(colorsCopy))

# 출력
print(answer)