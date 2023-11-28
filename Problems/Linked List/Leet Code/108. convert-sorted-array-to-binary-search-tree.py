# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def sortedArrayToBST(self, nums):
#         self.out = []
#         self.root = nums[len(nums)//2]
#         self.l = nums[:len(nums)//2]
#         self.r = nums[(len(nums)//2) +1:]
#         print(obj.returnDSA(self.root,self.l,self.r))
        
    
#     def returnDSA(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         if len(self.left)==1:
#             self.out.append(self.left)
            
#             self.out.append(self.val)
#         else:
#             obj.sortedArrayToBST(self.left)
        
#         if len(self.right)==1:
#             self.out.append(self.right)
            
#         else:
#             obj.sortedArrayToBST(self.right)
    
# obj = Solution()
# obj.sortedArrayToBST([-10,-3,0,5,9])