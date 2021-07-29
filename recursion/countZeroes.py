def countZeroes(n):
    ''' T-->O(logN) '''
    if n==0:
        return 0

    x = n%10
    n = n//10
    smallOutput = countZeroes(n)
    if x == 0:
        output = 1+ smallOutput
    else:
        output = smallOutput 

    return output

n = int(input())
print(countZeroes(n))