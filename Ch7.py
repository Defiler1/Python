# code 7.1
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
   print('runtime =', end - start)

run_combination(30,20)