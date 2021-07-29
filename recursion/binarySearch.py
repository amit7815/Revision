def binarySearch(A, x, si, ei):
    if si > ei: # when the list is empty
        return -1
    mid = (si+ei)//2
    if A[mid] == x:
        return mid
    elif A[mid] > x:
        smallOut = binarySearch(A, x, si, mid-1)
        return smallOut
    else:
        smallOut = binarySearch(A, x, mid+1, ei)
        return smallOut


a = [int(ele) for ele in input().split()]
n = len(a)
x = int(input())
print(binarySearch(a, x, 0, n-1))