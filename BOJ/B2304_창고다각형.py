# 입력
n = int(input())
list = [list(map(int, input().split())) for _ in range(n)]

# 정렬
list.sort()

area = 0

# 왼쪽->오른쪽 탐색
nowX = list[0][0]
nowH = list[0][1]
maxH = nowH
maxX = nowX
for i in range(1, len(list)):
  if (nowH<list[i][1]):
    area += nowH * (list[i][0]-nowX)
    nowH = list[i][1]
    nowX = list[i][0]
    maxH = nowH
    maxX = nowX

# 오른쪽 -> 왼쪽 탐색
nowX = list[len(list)-1][0]
nowH = list[len(list)-1][1]
for i in range(len(list)-1, -1, -1):
  if (nowH<list[i][1]):
    area += nowH * (nowX-list[i][0])
    nowH = list[i][1]
    nowX = list[i][0]

  # 가운데 최댓값 기둥 추가
  if (nowH==maxH): 
    area += (nowX-maxX+1)*maxH
    break

# 출력
print(area)