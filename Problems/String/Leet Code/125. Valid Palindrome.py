s='a.'
new_s = ''
s_rev = ''
for i in s:
  if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 48 and ord(i) <= 57):
    new_s += i
    s_rev = i + s_rev

if new_s.lower() == s_rev.lower():
  print('palind')
else:
  print('no')