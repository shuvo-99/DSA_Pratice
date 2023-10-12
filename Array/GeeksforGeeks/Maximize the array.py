class Solution:
    
    @staticmethod
    def reslist(a1,a2,l,l2):
        for i in a2:
            if (i in l) and (i not in l2):
                  
                l2.append(i)
        for i in a1:
            if (i in l) and (i not in l2):
                l2.append(i)
        return l2
    
    def maximizeArray(self, arr1, arr2, n):
        # code here
        l = []
        l2=[]
        a1 = arr1.copy()
        a2 = arr2.copy()
        arr1.sort(reverse=True)
        arr2.sort(reverse=True)
        while True:
            for i in range(len(arr2)):
                for j in range(len(arr1)):
                    if arr2[i] >= arr1[j]:
                        if len(l)<5:
                          if arr2[i] not in l:
                            l.append(arr2[i])
                            break
                        else:
                            r = Solution.reslist(a1,a2,l,l2)
                            return r
                            
                    
                    else:
                        if len(l)<5:
                          if arr1[j] not in l:
                            l.append(arr1[j])
                            continue
                        else:
                            r = Solution.reslist(a1,a2,l,l2)
                            return r
    

if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = 5
        arr1 = [7, 4, 8, 0, 1]
        arr2 = [9, 7, 2, 3, 6]
        ob = Solution()
        ans = ob.maximizeArray(arr1, arr2, n)
        for i in ans:
            print(i,end=" ")
        print()
        tc -= 1


# Alternate soln:

# from queue import PriorityQueue

# class Solution:
#     def maximizeArray(self,arr1, arr2, n):
#         temp1 = arr1.copy()
#         temp2 = arr2.copy()
    
#         # Sorting in descending order
#         temp1.sort(reverse=True)
#         temp2.sort(reverse=True)
    
#         i, j = 0, 0
#         ust = set()
#         count = 0
    
#         while i < n and j < n:
#             if temp1[i] > temp2[j]:
#                 if temp1[i] not in ust:
#                     ust.add(temp1[i])
#                     count += 1
#                 i += 1
#             else:
#                 if temp2[j] not in ust:
#                     ust.add(temp2[j])
#                     count += 1
#                 j += 1
    
#             if count == n:
#                 break
    
#         if count != n:
#             while j < n:
#                 if temp2[j] not in ust:
#                     ust.add(temp2[j])
#                     count += 1
#                 j += 1
#                 if count == n:
#                     break
    
#         if count != n:
#             while i < n:
#                 if temp1[i] not in ust:
#                     ust.add(temp1[i])
#                     count += 1
#                 i += 1
#                 if count == n:
#                     break
    
#         res = []
#         for num in arr2:
#             if num in ust:
#                 res.append(num)
#                 ust.remove(num)
    
#         for num in arr1:
#             if num in ust:
#                 res.append(num)
#                 ust.remove(num)
    
#         return res