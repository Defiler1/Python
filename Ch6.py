import random
from random import randrange
import time

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
def bin_search_OX3(ss,x):
   mid = len(ss) // 2
   return ss != [] and \
      (x == ss[mid] or \
      x < ss[mid] and bin_search_OX3(ss[:mid],x) or \
      bin_search_OX3(ss[mid + 1:],x))

# s = [3,5,8,7,4,6,1,9,2]
# s.sort()
# print(bin_search_OX3(s,5))
# print(bin_search_OX3(s,8))

# code 6-12
def bin_search(ss, key):
   low = 0
   high = len(ss) - 1
   while low <= high:
      mid = (high + low) // 2
      if key == ss[mid]:
         return mid
      elif key < ss[mid]:
         high = mid - 1
      else:
         low = mid + 1
   return None

# s = [3,5,8,7,4,6,1,9,2]
# s.sort()
# print(bin_search(s,5))
# print(bin_search(s,8))

# code 6-13
# print('Now, go!')
# start = time.perf_counter()
# print('Start at', start)
# time.sleep(5)
# finish = time.perf_counter()
# print('Finish at', finish)
# print('Total =', finish - start, 'secs')

# code 6-14
# print('Preparing data for seq_search. Please, wait a moment...')
# data = random.sample(range(1000), 800)

# print('Testing seq_search function begins...')
# for _ in range(5):
#    x = randrange(100)
#    start = time.perf_counter()
#    index = seq_search(data, x)
#    finish = time.perf_counter()
#    print(x, 'is found at', index, 'in', finish - start, 'secs')

# print('Preparing data for bin_search. Please, wait a moment...')
# data.sort()
# for _ in range(5):
#    x = randrange(100)
#    start = time.perf_counter()
#    index = seq_search(data, x)
#    finish = time.perf_counter()
#    print(x, 'is found at', index, 'in', finish - start, 'secs')

# print('Testing bin_search function begins...')
   

# t = open('input.txt', 'r') # python3 이후로는 ANSI 인코딩만 지원 utf-8 파일은 open('input.txt', 'r', 'utf-8')와 같이 사용
# print(t.read(1))
# print(t.read(30))
# print(t.readline(30)) # 파일 한 줄 단위로 읽을때 편리하게 사용
# print(t.readline())
# print(t.readline())
# print(t.readline())
# t.close()

# t = open('input.txt', 'w') # 'w' -> 원래 있던 내용은 삭제하고 새로 씀
# t.write('새 나라의 어린이는 일찍 일어납니다.\n')
# t.write('잠꾸러기 없는 나라\n')
# t.write('우리나라 좋은 나라')
# t.write('새 나라의 어린이는 일찍 일어납니다.\n잠꾸러기 없는 나라\n우리나라 좋은 나라')
# t.close()

# code 6-15 **
def find_1st(filename,x):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   position = text.find(x)
   if position == -1:
      outfile.write(x + ' is not found.\n')
   else:
      outfile.write(x + ' is at ' + str(position) + 'the 1st time.\n')
   outfile.close()
   infile.close()
   print('Done')


# find_1st('article.txt','computer')    # at 3269 the 1st time.
# find_1st('article.txt','Whole Earth') # at 10735 the 1st time.
# find_1st('article.txt','Apple')       # at 4380 the 1st time.
# find_1st('article.txt','apple')       # not found.


# code 6-16 두 번째로 나타나는 문자열 찾기
def find_2nd(filename, x):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   position = text.find(x)
   position = text.find(x,position + 1)
   if position == -1:
      outfile.write(x + ' is not found.\n')
   else:
      outfile.write(x + ' is at ' + str(position) + " the 2nd time.\n")
   outfile.close()
   infile.close()
   print('Done')


# find_2nd('article.txt', 'computer')
# find_2nd('article.txt','Whole Earth')
# find_2nd('article.txt','Apple')     
# find_2nd('article.txt','apple') 

# code 6-17
def find_last(filename, x):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   position = text.rfind(x)
   if position == -1:
      outfile.write(x + ' is not found.\n')
   else:
      outfile.write(x + " is at " + str(position) + "the last time.\n")
   outfile.close()
   infile.close()
   print('Done')

# find_last('article.txt', 'computer')
# find_last('article.txt','Whole Earth')
# find_last('article.txt','Apple')     
# find_last('article.txt','apple') 


# code 6-18
def find_all(filename, x):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   position = text.find(x)
   if position == -1:
      outfile.write(x + ' is not found\n')
   outfile.write(x + ' is at ')
   while position != -1:
      outfile.write(str(position) + ', ')
      position = text.find(x, position + 1)
   outfile.close()
   infile.close()
   print('Done')


# find_all('article.txt', 'computer')
# find_all('article.txt','Whole Earth')
# find_all('article.txt','Apple')     
# find_all('article.txt','apple') 


# code 6-19
def find_all_count(filename, x):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   position = text.find(x)
   count = 0
         
   while position != -1:
      count += 1
      position = text.find(x, position + 1)

   outfile.write(str(count) + ' time(s)')
   outfile.close()
   infile.close()
   print('Done')

# find_all_count('article.txt', 'computer')
# find_all_count('article.txt','Whole Earth')
# find_all_count('article.txt','Apple')     
# find_all_count('article.txt','apple') 

# code 6-20
def find_quotes_all(filename):
   infile = open(filename, 'r')
   outfile = open('result.txt', 'w')
   text = infile.read()
   count = 0
   begin = text.find('"')
   while begin != -1:
      (quote, end, text) = text[begin+1:].partition('"')
      outfile.write('"' + quote +'"\n\n')
      count += 1
      begin = text.find('"')

   outfile.write('There are ' + str(count) + " quotes in total.")
   outfile.close()
   infile.close()
   print('Done')

# find_quotes_all('article.txt')

# code 6-20
def greatest(ns):
   def loop(ns, top):
      if ns != []:
         if ns[0] > top:
            return loop(ns[1:], ns[0])
         else:
            return loop(ns[1:], top)
      else:
         return top
         
   if len(ns) == 0:
      return None
   else:
      return loop(ns[1:], ns[0])
   

# print(greatest([5,2,3,6,4,3,7,5,8,2]))    # 8

def greatest2(ns):
   if len(ns) == 0:
      return None
   else:
      top = ns[0]
      ns = ns[1:]
      while ns != []:
         if ns[0] > top:
            top = ns[0]
         ns = ns[1:]
      return top

# print(greatest2([5,2,3,6,4,3,7,5,8,2]))    # 8


def greatest3(ns):
   if len(ns) == 0:
      return None
   else:
      top = ns[0]
      for i in ns:
         if i > top:
            top = i

   return top

# print(greatest3([5,2,3,6,4,3,7,5,8,2]))    # 8


# code 6-21
def rankith(ns, i):
   
   if len(ns) == 0:
      return None
   else:
      top = max(ns)
      for n in range(i - 1):
         ns.remove(top)
         top = max(ns)

      return top

# print(rankith([5,2,3,6,4,3,7,5,8,2], 1))   # 8
# print(rankith([5,2,3,6,4,3,7,5,8,2], 2))   # 7
# print(rankith([5,2,3,6,4,3,7,5,8,2], 4))   # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],5))    # 5
# print(rankith([5,2,3,6,4,3,7,5,8,2],6))    # 4
# print(rankith([5,2],2))                    # 2
# print(rankith([5],1))                      # 5
# print(rankith([],1))                       # None


# code 6-22
def remove(c,s):
   if s != '':
      if s[0] != c:
         return s[0] + remove(c,s[1:])
      else:
         return remove(c,s[1:])
   else:
      return ''

# print(remove('a', 'abracadabra'))   #brcdbr
# print(remove('z', 'abracadabra'))   #abracadabra


def remove2(c,s):
   def loop(s,result):
      if s != '':
         if s[0] != c:
            result += s[0]
            return loop(s[1:],result)
         else:
            return loop(s[1:],result)
      else:
         return result

   return loop(s,'')

# print(remove2('a', 'abracadabra'))   #brcdbr
# print(remove2('z', 'abracadabra'))   #abracadabra


def remove3(c,s):
   result = ''
   while s != '':
      if s[0] != c:
         result += s[0]
      s = s[1:]
   return result

# print(remove3('a', 'abracadabra'))   #brcdbr
# print(remove3('z', 'abracadabra'))   #abracadabra


def remove4(c,s):
   result = ''
   for i in s:
      if c != i:
         result += i
   return result

# print(remove4('a', 'abracadabra'))   #brcdbr
# print(remove4('z', 'abracadabra'))   #abracadabra


# code 6-23