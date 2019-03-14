def swap(A, a, b):
    temp = None
    temp = A[a]
    A[a] = A[b]
    A[b] = temp
    return


def partition(A, p):
    x = A[p]
    j = 0
    i = j - 1
    while j < p:
        if A[j] <= x:
            i += 1
            swap(A, i, j)
        j = j + 1
    swap(A, i + 1, p)
    return i + 1


def quicksort(A):
    if len(A) == 1 or len(A) == 0:
        return A
    else:
        r = len(A) - 1
        q = partition(A, r)
        left = A[:q]
        right = A[q:]
        first = quicksort(left)
        second = quicksort(right)
        return first + second


A = [1, 4, 3, 2, 0, 6, 8]
print (quicksort(A))
