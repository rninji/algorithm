def solution(n, tops):
    prev1 = 1
    prev2 = 1
    for i in range(len(tops)):
        if tops[i] == 0:
            tmp = prev1 * 2 + prev2
            prev2 = prev1 + prev2
            prev1 = tmp
        else:
            tmp = prev1 * 3 + prev2
            prev2 = prev1 * 2 + prev2
            prev1 = tmp
    return prev1%10007
