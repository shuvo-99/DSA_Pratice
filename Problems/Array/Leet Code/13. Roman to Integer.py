class Solution:
  def romanToInt(self, s):
    data = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500, 'M': 1000}
    val = 0
    val_l = []
    for i in range(len(s)):
      for k,v in data.items():
        if i == 0:
          if  s[i] == k:
            val_l.append(v)
            break

        else:
          if i == 1:
            if (s[i-1] == 'I') and (s[i] == 'V' or s[i] == 'C'):
              if s[i] == k: 
                val_l.pop()
                val_l.append(v-1)
                break
              
            elif (s[i-1] == 'X') and (s[i] == 'L' or s[i] == 'C') :
              if s[i] == k: 
                val_l.pop()
                val_l.append(v-10)
                break
            
            elif (s[i-1] == 'C') and (s[i] == 'D' or s[i] == 'M') :
              if s[i] == k:
                val_l.pop()
                val_l.append(v-100)
                break
            
            else:
              if s[i] == k:
                val_l.append(v) 
                break


          else:
            if (s[i-1] == 'I') and (s[i] == 'V' or s[i] == 'X'):
              if s[i] == k: 
                val_l.pop()
                val_l.append(v-1)
                break
              
            elif (s[i-1] == 'X') and (s[i] == 'L' or s[i] == 'C') :
              if s[i] == k:
                val_l.pop()
                val_l.append(v-10)
                break
            
            elif (s[i-1] == 'C') and (s[i] == 'D' or s[i] == 'M') :
              if s[i] == k:
                val_l.pop()
                val_l.append(v-100)
                break

            else:
              if  s[i] == k:
                val_l.append(v)
                break

    val = sum(val_l)

    print(val)
    return val


obj = Solution()
obj.romanToInt('MMCCCXCIX')