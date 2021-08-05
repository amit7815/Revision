'''You have give an array return legth of lis including first element and overall length of lis'''


# using recursion
def lis(li, i, n):
    if i == n:
        return 0, 0  # return including max and overall

    including_max = 1
    for j in range(i+1, n):
        if li[j] >= li[i]:
            further_including_max =1 + lis(li, j, n)[0]
            including_max = max(including_max, further_including_max)

    excluding_max = lis(li, i+1, n)[1]

    overall_max = max(including_max, excluding_max)

    return including_max, overall_max

# using Memoization
def lis2(li, i, n, dp):
    if i == n:
        return 0, 0

    including_max = 1
    for j in range(i+1, n):
        if li[j] >= li[i]:
            if dp[j] == -1:
                ans = lis2(li, j, n, dp)
                dp[j] = ans
                further_including_max = 1 + ans[0]
            else:
                further_including_max = 1 + dp[j][0]

            including_max = max(including_max, further_including_max)

    if dp[i+1] == -1:
        ans = lis2(li, i+1, n, dp)
        dp[i+1] = ans
        excluding_max = ans[1]
    else:
        excluding_max = dp[i+1][1]

    overall_max = max(including_max, excluding_max)

    return including_max, overall_max
    
    overall_max = max(including_max, excluding_max)

# using dyanamic programming 

# def lis3(li, n, i):
#     dp = [[0 for j in range(2)] for i in range(n+1)]
#     for i in range(n-1, -1, -1):




li = list(map(int, input().split()))
n = len(li)
dp = [-1 for i in range(n+1)]
print(lis(li, 0, len(li)))
print(lis2(li, 0, len(li), dp))

