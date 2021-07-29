def mulOfTwoNo(m, n):
    ''' T --> O(N) '''
    if m == 0 or n == 0:
        return 0

    smallOutput = mulOfTwoNo(m, n-1)
    output = m + smallOutput
    return output

m,n = map(int, input().split())
print(mulOfTwoNo(m, n))
