def mergeSort(arr, way = 'forward'):
  if len(arr) > 1:
    mid = len(arr) //2
    L = arr[: mid]
    R = arr[mid:]

    mergeSort(L, way)
    mergeSort(R, way)

    i = j = k = 0
    while (i<len(L) and j<len(R)):
      
      if way == 'forward':
        if L[i] <= R[j]:
          arr[k] = L[i]
          i += 1
          k += 1
        else:
          arr[k] = R[j]
          j += 1
          k += 1
      
      else:
        if L[i] >= R[j]:
          arr[k] = L[i]
          i += 1
          k += 1
        else:
          arr[k] = R[j]
          j += 1
          k += 1

    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1
    
    while j < len(L):
      arr[k] = R[j]
      j += 1
      k += 1

def check(a, b, k):
  
  mergeSort(a)
  mergeSort(b, 'reverse')
  
  for i in range(len(a)):
    if a[i] + b[i] < k:
      return False

  return True

a = [ 2, 1, 3] 
b = [7, 9, 8] 
k = 10

if check(a,b,k):
  print('Yes')
else:
  print('No')
