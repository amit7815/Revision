def sumOfDigits(n):
    ''' T --> O(logN)'''
    if n <= 9:
        return n
    x = n%10
    n = n//10
    smallOutput = sumOfDigits(n)
    output = x + smallOutput
    return output


n = int(input())
print(sumOfDigits(n))