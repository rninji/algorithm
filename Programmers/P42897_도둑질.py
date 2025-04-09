def solution(money):
    answer = 0
    
    # 첫번째 집 턴 경우
    dp = [[0] * 2 for _ in range(len(money))]
    
    dp[1][1] = money[0]
    for i in range(2, len(money)):
        dp[i][0] = dp[i-1][1] + money[i] # i번째 집 터는 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]) # i번째 집 안 터는 경우
    
    answer1 = dp[len(money)-1][1] # 마지막 집 안 털기
    
    # 첫번째 집 안 턴 경우
    dp = [[0] * 2 for _ in range(len(money))]
    
    for i in range(1, len(money)):
        dp[i][0] = dp[i-1][1] + money[i] # i번째 집 터는 경우
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]) # i번째 집 안 터는 경우
    
    answer2 = max(dp[len(money)-1][0], dp[len(money)-1][1])
    
    return max(answer1, answer2)