# code 6-1
def seq_search_OX(s,x):
   if s != []:
      if s[0] == x:
         return True
      else:
         return seq_search_OX(s[1:], x)
   else:
      return False
   
# print(seq_search_OX([2,3,5,7], 4))
# print(seq_search_OX([2,3,5,7], 3))

# code 6-2
def seq_search_OX2(s,x):
   while s != []:
      if s[0] == x:
         return True
      else:
         s = s[1:]
   return False

# print(seq_search_OX2([2,3,5,7], 4))
# print(seq_search_OX2([2,3,5,7], 3))

# code 6-3
def seq_search_OX3(s,x):
   for i in s:
      if i == x:
         return True
   return False

# print(seq_search_OX3([2,3,5,7], 4))
# print(seq_search_OX3([2,3,5,7], 3))

# code 6-4
def seq_search_OX4(s,x):
   return s != [] and (s[0] == x or seq_search_OX4(s[1:],x))

# print(seq_search_OX4([2,3,5,7], 4))
# print(seq_search_OX4([2,3,5,7], 3))

# code 6-5
def seq_search(s,x):
   def loop(s,i):
      if s != []:
         if s[0] == x:
            return i
         else:
            return loop(s[1:], i + 1)
      else:
         return None 
   return loop(s,0)

# print(seq_search([2,3,5,7], 4))
# print(seq_search([2,3,5,7], 3))

# code 6-6
def seq_search2(s,x):
   def loop(i):
      if i < len(s):
         if s[i] == x:
            return i
         else:
            return loop(i + 1)
      else:
         return None
   return loop(0)

# print(seq_search2([2,3,5,7], 4))
# print(seq_search2([2,3,5,7], 3))

# code 6-7
def seq_search3(s,x):
   index = 0
   while index < len(s):
      if s[index] == x:
         return index
      else:
         index += 1
   return None

# print(seq_search3([2,3,5,7], 4))
# print(seq_search3([2,3,5,7], 3))

# code 6-8
def seq_search4(s,x):
   for i in range(len(s)):
      if s[i] == x:
         return i
   return None         

# print(seq_search4([2,3,5,7], 4))
# print(seq_search4([2,3,5,7], 3))

# code 6-9
def bin_search_OX(ss,x):
   if ss != []:
      mid = len(ss) // 2
      if x == ss[mid]:
         return True
      elif x < ss[mid]:
         return bin_search_OX(ss[:mid], x)
      else:
         return bin_search_OX(ss[mid+1:], x)
   else:
      return False

# s = [3,5,8,7,4,6,1,9,2]
# s.sort()
# print(bin_search_OX(s,5))
# print(bin_search_OX(s,8))


# code 6-10
def bin_search_OX2(ss,x):
   while ss != []:
      mid = len(ss) // 2
      if x == ss[mid]:
         return True
      elif x < ss[mid]:
         ss = ss[:mid]
      else:
         ss = ss[mid + 1:]
   return False

# s = [3,5,8,7,4,6,1,9,2]
# s.sort()
# print(bin_search_OX2(s,5))
# print(bin_search_OX2(s,8))

# code 6-11