
def mergeSort(arr):

  if len(arr) > 1:
    mid = len(arr)//2
    L = arr[ : mid]
    R = arr[mid: ]

    mergeSort(L)
    mergeSort(R)

    # ==== MERGE ====

    i = j = k = 0

    while (i<len(L) and j<len(R)):
      if L[i] <= R[j]:
        arr[k] = L[i]
        i+=1
        k+=1
      else:
        arr[k] = R[j]
        j+=1
        k+=1

    while (i<len(L)):
      arr[k] = L[i]
      i+=1
      k+=1

    while (j<len(R)):
      arr[k] = R[j]
      j+=1
      k+=1

# l1 = [2,8,15,18]
# l2 = [5,9,12,17,19,25]
# Merge(l1,l2)

arr = [9,3,7,5,6,4,8,2]
mergeSort(arr)
print(arr)


