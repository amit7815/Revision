def isSorted(A):
    l = len(A)
    if l == 0 or l== 1:
        return True
    
    if A[0] > A[1]:
        return False

    smallList = A[1:]
    smallerOut = isSorted(smallList)
    
    if smallerOut:
        return True
    else:
        return False

def isSorted1(A, si):
    l = len(A)
    if si >= l-1:
        return True
    if A[si] > A[si+1]:
        return False

    smallerOut = isSorted1(A, si+1)
    return smallerOut

A = [int(ele) for ele in input().split()]
print(isSorted(A))
print(isSorted1(A,0))