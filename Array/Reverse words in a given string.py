class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        s = S.split('.')
        s = s[-1::-1]
        res = '.'.join(s)
        return res
            
            




if __name__ == '__main__':
    t = 1
    for i in range(t):
        s = 'pqr.mno'
        obj = Solution()
        print(obj.reverseWords(s))

