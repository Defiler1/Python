# 7.1 설탕 최적 배송
# code 7.16
def minbags(n):
   if n > 1:
      if n == 2 or n == 3 or n == 5:
         return 1
      else:
         smallest = minbags(n-2)
         if n > 4:
            smallest = min(smallest, minbags(n-3))
         if n > 6:
            smallest = min(smallest, minbags(n-5))
      return 1 + smallest
   else:
      return 0

# print(minbags(1))
# print(minbags(2))
# print(minbags(3))
# print(minbags(4))
# print(minbags(5))
# print(minbags(6))
# print(minbags(7))

# 표채워풀기 버전
def minbags2(n):
   bags = [0,0,1,1,2,1,2]  # n이 0 ~ 6일때 
   if n > 6:
      i = 7
      while i <= n:
         smallest = min(bags[i-2], bags[i-3], bags[i-5])
         bags.append(smallest+1)
         i += 1
   return bags[n]

# print(minbags2(18))

# code 7.17
def run_minbags(n):
   from time import perf_counter
   start = perf_counter()
   answer = minbags(n)
   end = perf_counter()
   print('minbags(', n, ') => ', answer, sep='')
   print(round(end - start, 1), 'seconds')


# run_minbags(18)

# 7.2 달나라 토끼를 위한 구매대금 지불 도우미
def moon_rabbit(n):
   if n >= 1:
      if n == 1 or n == 2 or n == 5 or n == 7:
         return 1
      else:
         smallest = moon_rabbit(n - 1)
         if n > 3:
            smallest = min(smallest, moon_rabbit(n - 2))
         if n > 6:
            smallest = min(smallest, moon_rabbit(n - 5))
         if n > 8:
            smallest = min(smallest, moon_rabbit(n - 7))
      return 1 + smallest
   else:
      return 0

# print(moon_rabbit(1))
# print(moon_rabbit(2))
# print(moon_rabbit(3))
# print(moon_rabbit(4))
# print(moon_rabbit(5))
# print(moon_rabbit(6))