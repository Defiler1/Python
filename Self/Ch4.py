# 시그마
# code.4-1
def sigma(n):
   if n > 0:
      return sigma(n-1) + n
   else:
      return 0


def sigma2(n):
   def loop(n, total):
      if n > 0:
         return loop(n-1, n+total)
      else:
         return total
   return loop(n, 0)