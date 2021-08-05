''' 1. n--> n-1
    2. n--> n//2
    3. n--> n//3'''

import sys

# Using Recursion
def minStep(n):
    ans1, ans2 , ans3 = sys.maxsize, sys.maxsize, sys.maxsize 
    if n == 1:
        return 0

    ans1 = minStep(n-1)
    if n % 2 == 0:
        ans2 = minStep(n//2)
    if n % 3 == 0:
        ans3 = minStep(n//3)

    return 1 + min(ans1, ans2, ans3)

# Using Memoization
def minStep2(n, dp):
    ans1 ,ans2 ,ans3 = sys.maxsize, sys.maxsize, sys.maxsize
    if n == 1:
        return 0

    if dp[n-1] == -1:
        ans1 = minStep2(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    if n % 2 == 0:
        if dp[n//2] == -1:
            ans2 = minStep2(n//2, dp)
            dp[n//2] = ans2
        else:
            ans2 = dp[n//2]

    if n %3 == 0:
        if dp[n//3] == -1:
            ans3 = minStep2(n//3, dp)
            dp[n//3] = ans3
        else:
            ans3 = dp[n//3]

    
    return 1 + min(ans1, ans2, ans3)

def minStep3(n):
    dp = [-1 for i in range(n+1)]
    dp[1] = 0
    dp[0] = 0
    for i in range(2, n+1):
        ans1 = dp[i-1]
        if i % 2 == 0:
            ans2 = dp[i//2]
        else:
            ans2 = sys.maxsize
        if i % 3 == 0:
            ans3 = dp[i//3]
        else:
            ans3 = sys.maxsize
        dp[i] = 1 + min(ans1, ans2, ans3)
    return dp[i]
 
n = int(input())
dp = [-1 for i in range(n+1)]
print(minStep(n))
print(minStep2(n, dp))
print(minStep3(n))
