def partition(A, si, ei):
    ''' T -- O(N) '''
    pivot = A[si]
    # find No of elements smaller than pivot
    c = 0
    for i in range(si, ei+1):
        if A[i] < pivot:
            c = c+1
    
    A[si], A[si+c] = A[si+c], A[si]
    pivot_index = si+c

    i, j = si, ei
    while i<j:
        if A[i] < pivot:
            i = i+1
        elif A[j] >= pivot:
            j = j-1
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return pivot_index


def quickSort(A, si, ei):
    if si >= ei:
        return 

    pivot_index = partition(A, si, ei)
    quickSort(A,si, pivot_index-1)
    quickSort(A, pivot_index+1, ei)
    
    