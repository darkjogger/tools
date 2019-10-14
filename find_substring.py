def is_substring(short, long):
  length = len(short)
  if len(short)<= len(long):
    for i in range(len(long)-length+1):
      if long[i:(length+i)] == short :
        return True
  return False
  
  
is_substring('bad', 'abracadabra')
is_substring('dab', 'abracadabra')
is_substring('pony', 'pony')
is_substring('', 'balloon')
is_substring('balloon', '')

def count_substring(long, short):
  length = len(short)
  count = 0
  if len(short)<= len(long):
    for i in range(len(long)-length+1):
      if long[i:(length+i)] == short :
        count += 1
        if i< len(long)-length:
          i += length
  return count
  
def count_substring_v2(string, target):
    count = 0
    index = 0
    while index < len(string) - len(target) + 1:
        if string[index : index + len(target)] == target:
            count += 1
            index += len(target)   # <- look here
        else:
            index += 1
    return count
    
count_substring('love, love, love, all you need is love', 'love')

def locate_first(short,long):
  length = len(short)
  if len(short)<= len(long):
    for i in range(len(long)-length+1):
      if long[i:(length+i)] == short :
        return i
  return -1
"""  
>>> locate_first('ook', 'cookbook')
1
>>> locate_first('base', 'all your bass are belong to us')
-1
"""

def locate_all(long, short):
  length = len(short)
  count = []
  if len(short)<= len(long):
    for i in range(len(long)-length+1):
      if long[i:(length+i)] == short :
        count.append(i)
        if i< len(long)-length:
          i += length
  return count
  
"""
>>> locate_all('cookbook', 'ook')
[1, 5]
>>> locate_all('yesyesyes', 'yes')
[0, 3, 6]
>>> locate_all('the upside down', 'barb')
[]
"""
