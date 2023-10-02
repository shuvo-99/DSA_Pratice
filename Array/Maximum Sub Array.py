class Solution:

  def findSubarray(self,a, n):
    ans = []
    total_sum = 0
    start = 0
    max_sum = float('-inf')
    ans_start = start
    ans_end = 0

    for i in range(n):
        if a[i] < 0:
            total_sum = 0

        if total_sum == 0:
            start = i
        
        total_sum += a[i]
        
        if total_sum == max_sum:
            prev_max = ans_end - ans_start
            now = i - start
            
            if now > prev_max:
                ans_start = start
                ans_end = i
        
        if total_sum > max_sum:
            max_sum = max(max_sum, total_sum)
            ans_start = start
            ans_end = i
        
        if total_sum < 0:
            total_sum = 0
    
    for i in range(ans_start, ans_end + 1):
        ans.append(a[i])
    
    if not ans:
        ans.append(-1)
    
    return ans
			
if __name__ == '__main__':
	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int, input().strip().split()))
		ob = Solution()
		ans=ob.findSubarray(a, n)
		for x in ans:
			print(x, end=" ")
		print()
		tc=tc-1
		


# start = 0       
# for i in range(n):
#     if a[i]<0:
#         start = i+1

#     elif a[i]>=0:
        
#         if sum(a[start:i+1]) > sum(a[i+1:]):
#             return a[start:i+1]
#         elif sum(a[start:i+1]) == sum(a[i+1:]):
#             if len(a[start:i+1]) > len(a[i+1:]):
#                 return a[start:i+1]
#             elif len(a[start:i+1]) < len(a[i+1:]):
#                 return a[i+1:]
#             else:
#                 if a[0] < a[i+1]:
#                     return a[start:i+1]
#                 elif a[0] > a[i+1]:
#                     return a[i+1:]