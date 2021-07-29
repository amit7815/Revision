def lastIndex(A, x):
    l = len(A)
    if l == 0:
        return -1
    smallList = A[1:]
    smallOut = lastIndex(smallList, x)
    if smallOut == -1:
        if A[0] == x:
            return 0
        else:
            return -1
    else:
        return smallOut + 1

def lastIndex1(A, x, si):
    l = len(A)
    if si == l:
        return -1
    smallOut = lastIndex1(A,x, si+1)
    if smallOut == -1:
        if A[si] == x:
            return 0
        else:
            return -1
    else:
        return smallOut + 1   

A = [int(ele) for ele in input().split()]
x = int(input())
print(lastIndex(A, x))
print(lastIndex1(A, x,0))


    