class Solution:
    def removeElement(self, nums, val):
        i = 0
        while i <len(nums):
            if nums[i] == val :
                nums.remove(nums[i])
                
            else:
                i+=1
              
        return len(nums)
        
obj = Solution()
print(obj.removeElement([0,1,2,2,3,0,4,2], 2))