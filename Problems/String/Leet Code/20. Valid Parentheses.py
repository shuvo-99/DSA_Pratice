#  ===== Process 1 =====

def isValid(s):
  stack = []
  if len(s) == 0 or len(s) == 1:
    return False
  for i in s:
    if (s[0] == ')') or (s[0] == '}') or (s[0] == ']'):
      return False
    if (i == '(') or (i == '{') or (i == '['):
      stack.append(i)
      continue
    if len(stack) != 0:
      if (stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}') or (stack[-1] == '[' and i == ']'):
        stack.pop()
      elif (i == ')') or (i == '}') or (i == ']'):
        return False
    else:
      if (i == ')') or (i == '}') or (i == ']'):
        return False
  if len(stack) == 0:
    return True
  return False

s = "()"
print(isValid(s))


#  ===== Process 1 =====

def isValid(s):
  open = []
  dict = {
  '}':'{',
  ')': '(',
  ']': '['
  }
  for i in s:
      if i in dict:
          if open and open[-1] == dict[i]:
              open.pop()
          else:
              return False
      else:
          open.append(i)
  return True if not open else False

s = "(())"
print(isValid(s))


