class Solution:
    def romanToDecimal(self, str_):
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        i = 0
        while i < len(str_) - 1:
            ch1 = str_[i]
            ch2 = str_[i + 1]
            if m[ch1] >= m[ch2]:
                ans += m[ch1]
                i += 1
            else:
                ans += (m[ch2] - m[ch1])
                i += 2

        if i < len(str_):
            ans += m[str_[i]]

        return ans
          

if __name__=='__main__':
    t = 1
    for _ in range(t):
        ob = Solution()
        S = 'XIX'
        print(ob.romanToDecimal(S))



