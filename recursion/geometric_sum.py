''' Given K , find the geometric sum i.e 1+1/2+1/4+1/8+......+1/2^k  using recursion '''

def geometricSum(k):
    '''T -->O(N)'''
    if k == 0:
        return 1
    
    smallOutput = geometricSum(k-1)
    output = 1/(2**k)  + smallOutput
    return output

k = int(input())
print(geometricSum(k))
