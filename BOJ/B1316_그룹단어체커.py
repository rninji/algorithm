# 입력
N = int(input())
words = []
for _ in range(N):
  words.append(input())

# 풀이
answer = 0

for word in words: # 각 단어 체크
  chk = [0]*26
  prev = -1
  answer += 1
  for w in word: # 각 알파벳 체크
    now = ord(w) - 97
    if prev == now:
      continue
    elif chk[now] != 0:
      answer -= 1
      break
    prev = now
    chk[now] = 1

# 출력
print(answer)