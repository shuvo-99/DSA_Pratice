class Solution:
  def longestCommonPrefix(self, strs):
  # def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = ''
    if len(strs)==1:
      print(strs[0])
      return strs[0]
    else:
      for  i in range(len(strs)-1):
        j=0
        pre = ''
        while j>=0:
          if len(strs[i]) == 0  or len(strs[i+1]) == 0:
              print()
              return ''
          
          if i == 0:
            
            if j < len(strs[i]) and j < len(strs[i+1]):
              if (strs[i][j] == strs[i+1][j]):
                prefix += strs[i][j]
                j+=1
              else:
                break
            else:
              break
          elif len(prefix) == 0:
            # print(prefix)
            return prefix
          else:

            if len(pre) > len(prefix):
              break

            
            elif j < len(strs[i]) and j < len(strs[i+1]):
              if (strs[i][j] == strs[i+1][j]) and (strs[i][j] in prefix):
                pre += strs[i][j]
                j+=1
                
              else:
                prefix = pre 
                break
            else:
              prefix = pre 
              break
      print(prefix)
      return prefix
          

obj = Solution()
obj.longestCommonPrefix(["abc"])
obj.longestCommonPrefix(["abab","aba",""])
obj.longestCommonPrefix(["acc","aaa","aaba"])
obj.longestCommonPrefix(["ac","ac","a","a"])