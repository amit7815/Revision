# Using Recursion
def fib(n):
    ''' T -- O(2^n)'''
    if n == 0 or n == 1:
        return n

    ans1 = fib(n-1)
    ans2 = fib(n-2)
    ans = ans1 + ans2
    return ans


# Using Memoization
def fib1(n, dp):
    if n == 0 or n == 1:
        return n

    if dp[n-1] == -1:
        ans1 = fib1(n-1, dp)
        dp[n-1] = ans1
    else:
        ans1 = dp[n-1]

    if dp[n-2] == -1:
        ans2 = fib1(n-2, dp)
        dp[n-2] = ans2
    else:
        ans2 = dp[n-2]

    return ans1 + ans2

# using Dyanamic programming
def fib2(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


n = int(input())
dp = [-1 for i in range(n+1)]
print(fib(n))
print(fib1(n, dp))
print(fib2(n))
