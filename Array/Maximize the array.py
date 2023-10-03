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
        arr1.sort()
        arr2.sort()
        while True:
            for i in range(len(arr2)-1,0,-1):
                for j in range(len(arr1)-1,0,-1):
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
                            break
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

# } Driver Code Ends