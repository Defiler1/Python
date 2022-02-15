# 피보나치 수열
# code 7.1
from re import L
from matplotlib.pyplot import step


def fib(n):
   if n > 1:
      return fib(n-1) + fib(n-2)
   else:
      return n

# print(fib(5))


# code 7.2
def run_fib(n):
   from time import perf_counter
   start = perf_counter()
   answer = fib(n)
   finish = perf_counter()
   print('fib(', n, ') => ',answer, sep = '')
   print(round(finish-start,4), 'seconds')

# run_fib(12)   
# run_fib(24)   
# run_fib(36)   


# code 7.3
def fib2(n):
   if n > 1:
      i = 2
      a, b = 0, 1          # fib(0), fib(1)
      while i <= n:
         a, b = b, a + b   # fib(1), fib(2) -> fib(2), fib(3) -> fib(3), fib(4)...
         i += 1
      return b
   else:
      return n 

# print(fib2(36))


# code 7.4
def fib3(n):
   if n > 1:
      a, b = 0, 1
      for _ in range(2, n + 1):
         a, b = b, a + b
      return b
   else:
      return n


# code 7.5
def fibseq(n):
   fibs = [0,1]
   for i in range(2, n+1):
      fibs.append(fibs[i-1] + fibs[i-2])
   return fibs

# print(fibseq(2))

# code 7.6
def fib4(n):
   return fibseq(n)[-1]

# print(fib4(5))

# code 7.7
def combination(n, r):
   if r != 0 and r != n:
      return combination(n-1, r-1) + combination(n-1, r)
   else:
      return 1


# print(combination(30, 20))


# 실행시간 측정 함수
def run_combination(n, r):
   from time import perf_counter
   start = perf_counter()
   result = combination(n, r)
   end = perf_counter()
   print('result=', result)
   print('runtime =', round(end - start, 4))

# run_combination(30,20)

# 파스칼의 삼각형

# code 7.8
def comb_pascal(n,r):
   rowO = [1 for _ in range(r+1)]   # 첫 가로줄
   matrix = [rowO] + [[1] for _ in range(n-r)]  # 행렬
   for i in range(1, n-r+1):
      for j in range(1, r+1):
         newvalue = matrix[i][j-1] + matrix[i-1][j]
         matrix[i].append(newvalue)
   return matrix[n-r][r]


def run_comb_pascal(n,r):
   from time import perf_counter
   start = perf_counter()
   result = comb_pascal(n,r)
   end = perf_counter()
   print('result:', result)
   print('runtime:', round(end-start,4))

# run_comb_pascal(30,3)  # 4060 - 0.0 seconds
# run_comb_pascal(30,27) # 4060 - 0.0 seconds
# run_comb_pascal(30,7)  # 2035800 - 0.0001 seconds
# run_comb_pascal(30,23) # 2035800 - 0.0 seconds
# run_comb_pascal(30,10) # 30045015 - 0.0001 seconds
# run_comb_pascal(30,20) # 30045015 - 0.0001 seconds
# run_comb_pascal(30,15) # 155117520 - 0.0001 seconds
# run_comb_pascal(6,4) # 15 - 0.0

# code 7.9
def comb_pascal2(n,r):
   vector = [1 for _ in range(r+1)]
   for _ in range(1, n-r+1):
      for j in range(1, r+1):
         vector[j] = vector[j-1] + vector[j]
   return vector[r]


# code 7.10 **
def minsteps(n):
   if n > 1:
      steps = minsteps(n-1)
      print('1번', steps)
      if n % 2 == 0:
         steps = min(steps, minsteps(n//2))
         print('2번', steps)
      if n % 3 == 0:
         steps = min(steps, minsteps(n//3))
         print('3번', steps)
      return 1 + steps
   else:
      return 0

# print(minsteps(2))
# print(minsteps(4))

# code 7.12
def memo_minsteps(n):
   memo = [0 for _ in range(n+1)]
   def loop(n):
      if n > 1:
         if memo[n] == 0:
            steps = loop(n-1)
            if n % 2 == 0:
               steps = min(steps, loop(n // 2))
            if n % 3 == 0:
               steps = min(steps, loop(n // 3))
            memo[n] = steps + 1
         return memo[n]
      else:
         return 0
   return loop(n)

# print(memo_minsteps(10))


# code 7.13
def minsteps(n):
   memo = [0 for _ in range(n+1)]
   for i in range(2, n+1):
      steps = memo[i-1]
      if i % 2 == 0:
         steps = min(steps, memo[i//2])
      if i % 3 == 0:
         steps = min(steps, memo[i//3])
      memo[i] = steps + 1
   return memo[n]
   
# print(minsteps(3))       # 1
# print(minsteps(4))       # 2
# print(minsteps(7))       # 3
# print(minsteps(10))      # 3
# print(minsteps(23))      # 6
# print(minsteps(237))     # 8
# print(minsteps(317))     # 10
# print(minsteps(514))     # 8
# print(minsteps(711))     # 9
# print(minsteps(908))     # 11
# print(minsteps(1000))    # 9
# print(minsteps(2020))    # 10
# print(minsteps(1111111)) # 19

# 7.4 하노이의 탑
# code 7.14
# n - 원반개수 source - 출발점 desin - 도착점 temp - 임시말뚝
def tower_of_hanoi(n, source, destin, temp):
   if n > 1:
      tower_of_hanoi(n-1, source, temp, destin)
      print('Move a disk from', source, 'to', destin)
      tower_of_hanoi(n-1, temp, destin, source)
   else:
      print('Move a disk from', source, 'to', destin)

# A - 출발 B - 임시 C - 도착
tower_of_hanoi(3, 'A', 'C', 'B')