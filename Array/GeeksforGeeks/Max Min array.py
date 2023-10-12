class Solution:
    def findSum(self,A,N): 
        # RAW CODING
        max0 = A[0]
        min0 = A[0]
        for i in range(1,N):
          if A[i] > max0:
              max0 = A[i]

          if A[i] < min0:
              min0 = A[i]

        res = min0 + max0
        return res  
            
t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))