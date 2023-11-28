class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            elif target < nums[i]:
                return i
        return i+1
        
obj = Solution()
print(obj.searchInsert([1,3,5,6], 7))