def merge(A1,A2,A):
    i,j,k = 0,0,0
    while i < len(A1) and j < len(A2):
        if A1[i] < A2[j]:
            A[k] = A1[i]
            i += 1
            k += 1

        else:
            A[k] = A2[j]
            j += 1
            k += 1
    
    while i < len(A1):
        A[k] = A1[i]
        k += 1
        i += 1
    
    while j < len(A2):
        A[k] = A2[j]
        k += 1
        j += 1




def merge_sort(A):
    if len(A) == 0 or len(A) == 1:
        return

    mid = len(A)//2
    A1 = A[:mid]
    A2 = A[mid:]
    merge_sort(A1)
    merge_sort(A2)
    merge(A1, A2, A)


A = [int(ele) for ele in input().split()]
merge_sort(A)
print(A)