def mergersort(arr):
    if len(arr)<2:
        return arr
    else:
        mid = int(len(arr)/2)
        left = mergersort(arr[:mid])
        right = mergersort(arr[mid:])
        return merge(left,right)

def merge(L,R):
    A = []
    i=0
    j=0
    while i<len(L) and j<len(R):
        if L[i]<= R[j]:
            A.append(L[i])
            i+=1
            print(A)
        else:
            A.append(R[j])
            j+=1
            print(A)
    A+=L[i:]
    A+=R[j:]
    return A
print(mergersort([1,3,2,4,-1]))

