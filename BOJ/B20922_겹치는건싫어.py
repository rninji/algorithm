# 입력
N, K = map(int, input().split())
a = list(map(int, input().split()))
cnt_list = [0] * 100001

# 풀이
ans = 0
st = 0
ed = 0
for i in range(N):
    ed = i+1
    cnt_list[a[i]] += 1
    if cnt_list[a[i]] <= K:
        ans = max(ans, ed-st)
    while cnt_list[a[i]] > K:
        cnt_list[a[st]] -= 1
        st += 1

# 출력
print(ans)
    