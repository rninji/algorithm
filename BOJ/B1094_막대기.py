# 입력
x = int(input())
list = []
list.append(64)

# 풀이
if(x==64):
  print(1)
  exit()
  
while(True):
  half = min(list)//2
  list.remove(min(list)) # 자른 막대 삭제
  list.append(half)
  list.append(half)
  if (x<=sum(list)-half):
    list.remove(min(list)) # 절반 하나 삭제
  if (sum(list)==x):
    break

# 출력
print(len(list))