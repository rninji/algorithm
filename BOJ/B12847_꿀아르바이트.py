# 입력
n, m = map(int, input().split())
T = list(map(int, input().split()))

# 풀이
firstPay = T[0:m]
maxPay = sum(firstPay)
pay = maxPay
for i in range(n-m):
    pay -= T[i]
    pay += T[i+m]
    maxPay = max(maxPay, pay)

# 출력
print(maxPay)