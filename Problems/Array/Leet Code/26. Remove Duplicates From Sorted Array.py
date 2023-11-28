class Solution:
    def removeDuplicates(self, nums):
        unique_list = []
        
        for i in nums:
            if i not in unique_list:
                unique_list.append(i)

        nums.clear()
        for i in unique_list:
            nums.append(i)
        
        return len(nums)

# Alternate Solution

class Solution:
    def removeDuplicates(self, nums):
        
        if len(nums)<2:
            return len(nums)
        
        pre = 0
        for cur in range(1,len(nums)):
            if nums[cur]!=nums[pre]:
                pre+=1
                nums[pre]=nums[cur]

        return pre+1