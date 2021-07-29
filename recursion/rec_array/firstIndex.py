def firstIndex(A, x):
    l = len(A)
    if l == 0:
        return -1
    if A[0] == x:
        return 0
    smallerList = A[1:]
    smallerOut = firstIndex(smallerList, x)

    if smallerOut == -1:
        return -1
    else:
        return smallerOut + 1


def firstIndex1(A, si, x):
    l = len(A)
    if si >= l:
        return -1
    if A[si] == x:
        return si
    smallOut = firstIndex1(A, si+1, x)
    return smallOut

A = [int(ele) for ele in input().split()]
x = int(input())
print(firstIndex(A,x))
print(firstIndex1(A,0,x))

