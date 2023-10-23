class Solution:
    def singleNumber(self, nums):
        nums.sort()
        
        i = 0
        while i<len(nums):

          if (i != len(nums)-1) and  (nums[i] == nums[i+1]):
            
            i+=2
          else:
             print(nums[i])
             return nums[i]
obj = Solution()
obj.singleNumber([4,1,2,1,2])