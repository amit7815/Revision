# Using Recursion

import math, sys
def minSquare(n):
    if n == 0:
        return 0

    root = int(math.sqrt(n))
    ans = sys.maxsize
    for i in range(1, root+1):
        curAns = 1 + minSquare(n-(i**2))
        ans = min(ans, curAns)
    return ans


# Using Memoization
def minSquare2(n, dp):
    if n == 0 :
        return 0

    root = int(math.sqrt(n))

    ans = sys.maxsize
    for i in range(1, root+1):
        curCheckValue = n-(i**2)
        if dp[curCheckValue] == -1:
            smallAns = minSquare2(curCheckValue, dp)
            dp[curCheckValue] = smallAns
            curAns = 1 + smallAns
        else:
            curAns = 1 + dp[curCheckValue]

        ans = min(ans, curAns)
    return ans


# using Dyanamic Programming
def minSquare3(n):
    dp = [-1 for i in range(n+1)]
    dp[0] = 0
    root = int(math.sqrt(n))
    for i in range(1, n+1):
        root = int(math.sqrt(i))
        ans = sys.maxsize
        for j in range(1, root+1):
            curAns = 1 + dp[i-(j**2)]
            ans = min(ans, curAns)
        dp[i] = ans
    return dp[n]



n = int(input())
dp = [-1 for i in range(n+1)]

print(minSquare2(n, dp))
print(minSquare3(n))
print(minSquare(n))
