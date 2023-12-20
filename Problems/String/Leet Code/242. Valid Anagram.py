# ===== Process 1 =====
 
def isAnagram(s, t):
  dict1={}
  dict2={}
  if len(s) != len(t):
    return False
  else:
    for i in s:
      if i in dict1:
        dict1[i] += 1
      else:
        dict1[i] = 1 
    for j in t:
      if j in dict2:
        dict2[j] += 1
      else:
        dict2[j] = 1 
    if dict1 == dict2:
      return True
    else:
      return False
    
s = 'rat'
t = 'cat'
print(isAnagram(s,t))


# ===== Process 2 =====
 
def isAnagram(s, t):
  if len(s) != len(t):
    return False
  dict1 = {}
  for i in s:
    if i in dict1:
      dict1[i] += 1
    else:
      dict1[i] = 1
  for j in t:
    if j in dict1:
      dict1[j] -= 1
    else: 
      return False
  
  for v in dict1.values():
    if v != 0:
      return False
  return True
  
s = "anagram"
t = "nagaram"
print(isAnagram(s,t))  

# ===== Process 3 =====
 
from collections import defaultdict 

def isAnagram(s, t):
    if len(s) != len(t):
        return False

    dic = defaultdict(int)

    for c1 in s:
        dic[c1] += 1 
    for c2 in t:
        dic[c2] -= 1

    for v in dic.values():
        if v!= 0:
            return False
    
    return True
  
s = "cat"
t = "rat"
print(isAnagram(s,t))  

# ===== Process 4 =====

from collections import Counter

def isAnagram(s, t):
    return Counter(s) == Counter(t)

s = "cat"
t = "rat"
print(isAnagram(s,t)) 