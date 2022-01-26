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
find_2nd('article.txt','apple') 

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

# find_2nd('article.txt', 'computer')
# find_2nd('article.txt','Whole Earth')
# find_2nd('article.txt','Apple')     
find_2nd('article.txt','apple') 
