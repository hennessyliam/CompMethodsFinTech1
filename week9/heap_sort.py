def find_min(A):
    for i in range(len(A)):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]

def find_max(A):
    for i in range(len(A)):
        max_idx = i
        for j in range(i+1, len(A)):
            if A[max_idx] < A[j]:
                max_idx = j
        A[i], A[max_idx] = A[max_idx], A[i]

def heap_sort(arr):
    n = len(arr)

