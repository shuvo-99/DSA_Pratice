#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        s = s.split('.')
        l=[]
        for i in s:
            res=''
            for j in i:
              res = j + res
            l.append(res)
        
        oup=''
        for i in l:
            oup+= i+'.'
        return oup[:-1]


if __name__ == '__main__':
    t = 1
    for _ in range(t):
        s = 'pqr.mno'
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
