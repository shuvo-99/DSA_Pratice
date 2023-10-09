class Solution:

	def reverseSubArray(self,arr, n, l, r):
          if l<r:
            for i in range(n):
              if i == l-1:
                  lft = arr[:i]
                  mid = arr[i:]
              elif i == r-1:
                  rgt = arr[i+1:]
                  mid = mid[:i-l+2]
                  
                  break
            mid = mid[-1::-1]
            arr.clear()
            for i in lft:
                arr.append(i)
            for i in mid:
                arr.append(i)
            for i in rgt:
                arr.append(i)
          
          # return arr




if __name__ == '__main__':
    tc = 1
    while tc > 0:
        n = 34
        arr = ['674', '665', '142', '712', '254', '869', '548', '645', '663', '758', '38', '860', '724', '742', '530', '779', '317', '36', '191', '843', '289', '107', '41', '943', '265', '649', '447', '806', '891', '730', '371', '351', '7', '102']
        l, r = [4,15]
        ob = Solution()
        ob.reverseSubArray(arr, n, l, r)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

