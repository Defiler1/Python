import random
from random import randrange
from re import search
import time

from chap6sol import test_search_widest_gap

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
def collect_dups(s):
   singles = ''
   duplicates = []
   for i in s:
      if i not in singles:
         singles += i
      else:
         if i not in duplicates:
            duplicates.append(i)
   return duplicates


# print(collect_dups('sophisticated'))
# # ['s', 'i', 't']
# print(collect_dups("I'm no angel."))
# # [' ', 'n']
# print(collect_dups("Stay Hungry. Stay Foolish."))
# # ['y', ' ', 'S', 't', 'a', 'o', '.']


# 6.5 아이소그램 확인
def isisogram(s):
   singles = ''
   for i in s:
      if i not in singles:
         singles += i
      else:
         return False
   return True

def isisogram(s):
   while s != '' and s[1:] != '':
      if s[0] in s[1:]:
         return False
      else:
         s = s[1:]
   return True

# print(isisogram(""))                 # True
# print(isisogram("a"))                # True
# print(isisogram("aa"))               # False
# print(isisogram("and"))              # True
# print(isisogram("hanyang"))          # False
# print(isisogram("playground"))       # True
# print(isisogram("uncopyrightables")) # True


# code 6-24
def isanagram(word1, word2):
   while word1 != '':
      if word1[0] in word2:
         index = word2.find(word1[0])
         word1 = word1[1:]
         word2 = word2[:index] + word2[index + 1:]
      else:
         return False
   return word2 == ''



# print(isanagram('',''))                 # True
# print(isanagram('z','z'))               # True
# print(isanagram('zz','z'))              # False
# print(isanagram('z','zz'))              # False
# print(isanagram('silent','listen'))     # True
# print(isanagram('silent','listens'))    # False
# print(isanagram('elvis','lives'))       # True
# print(isanagram('restful','fluster'))   # True
# print(isanagram('restfully','fluster')) # False
# print(isanagram('문전박대','대박전문'))  # True
# print(isanagram('', '대박전문'))        #  False


# 6.7 완전수 찾기
# 자신을 제외한 약수의 리스트를 모아주는 보조 함수
def collect_divisors(n):
   divisor = 2
   divisors = [1]
   while n / divisor >= 2:
      if n / divisor == n // divisor:
         divisors.append(divisor)
      divisor += 1
   return divisors

# print(collect_divisors(6)) # [1, 2, 3]
# print(collect_divisors(28)) # [1, 2, 4, 7, 14]
# print(collect_divisors(29)) # [1]


def find_perfects_upto(trys):
   perfectNum = []
   for i in range(2, trys + 1):
      if sum(collect_divisors(i)) == i:
         perfectNum.append(i)
   return perfectNum

# print(find_perfects_upto(10000))
# [6, 28, 496, 8128]


# code 6.25
def search_widest_gap(ss):
   if len(ss) == 0:
      return None, 0
   elif len(ss) == 1:
      return 0,0
   else:
      maxgap = 0
      index = 0
      for i in range(len(ss) - 1):
         gap = ss[i + 1] - ss[i]
         if gap > maxgap:
            maxgap = gap   
            index = i
      return index, maxgap
      



# print(search_widest_gap([]))                     # (None, 0)
# print(search_widest_gap([3]))                    # (0, 0)
# print(search_widest_gap([3,5,8,20,22]))          # (2, 12)
# print(search_widest_gap([3,5,8,20,22,34,37,40])) # (2, 12)


# code 6.26
def testsearch_widest_gap():
   db = random.sample(range(500), 100)
   print('Searching the widest gap..')
   db.sort()
   print(db)
   index, gap = search_widest_gap(db)
   print('The widest gap is:', gap)
   print('between', db[index], 'and', db[index+1])
   print('at', index)

# testsearch_widest_gap()


# code 6.27
def ascending(ns):
   if len(ns) < 2:
      return False
   else:
      while len(ns) >= 2:
         if ns[0] < ns[1]:
            ns = ns[1:]
         else:
            return False
      return True

# print(ascending([1,3]))                # True
# print(ascending([2, 3, 6, 8, 12, 17])) # True
# print(ascending([]))                   # False
# print(ascending([2]))                  # False
# print(ascending([3, 3, 3, 3, 3]))      # False
# print(ascending([1, 2, 2, 3]))         # False
# print(ascending([2, 3, 1]))            # False


# code 6.28 **
def sublists(ns):
    def get(k,ns):
        subs = []
        for i in range(len(ns)-k+1):
            subs.append(ns[i:i+k])
        return subs
    subs = [[]]
    for k in range(1,len(ns)):
        subs += get(k,ns)
    if ns != []:
        subs.append(ns)
    return subs

# print(sublists([])) 
# # [[]]
# print(sublists([1])) 
# # [[], [1]]
# print(sublists([1,2])) 
# # [[], [1], [2], [1, 2]]
# print(sublists([1,2,3])) 
# # [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
# print(sublists([1,2,3,4])) 
# # [[], [1], [2], [3], [4], [1, 2], [2, 3], [3, 4], [1, 2, 3], [2, 3, 4], [1, 2, 3, 4]]
# print(sublists([3,1,2])) 
# [[], [3], [1], [2], [3, 1], [1, 2], [3, 1, 2]]


# code 6.29
def ascending_sublists(ns):
   result = []
   for i in sublists(ns):
      if ascending(i):
         result.append(i)
   return result


# print(ascending_sublists([])) 
# # []
# print(ascending_sublists([1])) 
# # []
# print(ascending_sublists([1,2])) 
# # [[1, 2]]
# print(ascending_sublists([1,2,3])) 
# # [[1, 2], [2, 3], [1, 2, 3]]
# print(ascending_sublists([3,1,2])) 
# # [[1, 2]]
# print(ascending_sublists([1,3,2])) 
# # [[1, 3]]
# print(ascending_sublists([1,5,3,4,8,2,3,5])) 
# # [[1, 5], [3, 4], [4, 8], [2, 3], [3, 5], [3, 4, 8], [2, 3, 5]]



# code 6.30
def longest_ascending_sublist(ns):
      
   pass


# print(longest_ascending_sublist([1,5,3,4,8,2,3,5]))
# # [3, 4, 8]
# print(longest_ascending_sublist([]))
# # []
# sample = [59, 4, 38, 54, 33, 75, 19, 73, 49, 7, 86, 28, 54, 13, 6, 42, 97, 84, 26, 69, 86, 14, 79, 27, 68, 57, 35, 53, 92, 58, 68, 49, 93, 28, 31, 63, 51, 1, 44, 62, 14, 40, 53, 40, 5, 69, 81, 95, 58, 55, 90, 56, 91, 40, 55, 14, 65, 28, 37, 61, 66, 89, 26, 63, 98, 59, 7, 23, 34, 67, 77, 30, 49, 55, 31, 58, 10, 27, 15, 45, 42, 77, 11, 14, 9, 55, 88, 44, 53, 12, 54, 95, 25, 91, 29, 8, 25, 90, 34, 55]
# print(longest_ascending_sublist(sample))
# # [28, 37, 61, 66, 89]

