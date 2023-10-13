class Solution:
    def plusOne(self, nums1, m, nums2, n):
        
        for i in range(len(nums1)):
            if i>=m:
                nums1.pop()

        for i in range(len(nums2)):
            if i>=n:
                nums1.pop()

        for i in nums2:
            nums1.append(i)

        for i in range(len(nums1)):
            min_idx = i

            for j in range(i+1, m+n):
                if nums1[j] < nums1[min_idx]:
                    min_idx = j
                
            temp = nums1[i]
            nums1[i] = nums1[min_idx]
            nums1[min_idx] = temp
               
obj = Solution()
obj.plusOne([1,2,3,0,0,0], 3,[2,5,6],3)