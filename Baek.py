n, t, g = map(int, input().split())
# N - LED로 표현된 수, T - 버튼을 누를 수 있는 최대 횟수, G - 탈출을 위해 똑같이 만들어야 하는 수

def pushA(n):
   n += 1
   return n

def pushB(n):
   a = []
   if n == 0:
      return 0
   else:
      n *= 2
      for i in str(n):
         a.append(n)
      int(a[0]) - 1
      return n
