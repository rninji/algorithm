# 입력
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

# 풀이
answer = 0
nums.sort()
max = n-1
for i in range(max):
  for j in range(max, i, -1):
    if nums[i] + nums[j] >= x:
      max = j-1
    if nums[i] + nums[j] == x:
      answer += 1
      break

# 출력
print(answer)