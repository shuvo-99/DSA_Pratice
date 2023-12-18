def QuickSort(arr, left, right):
  if left < right:
    j = partition(arr, left, right)
    QuickSort(arr, left, j)
    QuickSort(arr, j+1, right)

def partition(arr, l, r):
  pivot = arr[l]
  i = l
  j = r

  while (i < j):
    if arr[i] <= pivot:
      i +=1
    
    if arr[j] > pivot:
      j -=1
    
    if (i < j):
      temp = arr[j]
      arr[j] = arr[i]
      arr[i] = temp

  temp = arr[j]
  arr[j] = arr[l]
  arr[l] = temp
  return j
  

arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]

QuickSort(arr, 0, len(arr)-1)
print(arr)