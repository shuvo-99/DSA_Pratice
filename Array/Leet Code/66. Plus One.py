class Solution:
    def plusOne(self, digits):
        res = ''
        for i in digits:
            res+=str(i)
        res = int(res)+1
        digits.clear()
        for i in str(res):
            digits.append(int(i))
        return digits
        
obj = Solution()
print(obj.plusOne([1,2,3]))