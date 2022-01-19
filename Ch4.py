# p166  code 4-10 실습 4.1

# def sumrange(m,n):
#     if(m <= n):
#         return m + sumrange(m + 1, n)
#     else:
#         return 0

# print(sumrange(3,4))
# code 4-11 꼬리 재귀

# def sumrange2(m,n):
#     def loop(m, total):
#         if m <= n:
#             return loop(m+1, m +total)
#         else:
#             return total
#     return loop(m,0)

# print(sumrange2(3,4))

# code 4-12
# def sumrange3(m,n):
#     total = 0
#     while m <= n:
#         total += m
#         m += 1
#     return total

# print(sumrange3(3,4))

# code 4-13
# def power(b,n):
#     if n > 0:
#         return b * power(b, n-1)
#     else:
#         return 1

# print(power(2,5))


# code 4-14 꼬리재귀
# def power2(b,n):
#     def loop(b,n,prod):
#         if n > 0:
#             return loop(b,n-1,b*prod)
#         else:
#             return prod
#     return loop(b,n,1)

# print(power2(2,5))

# code 4-15
# def power3(b,n):
#     def loop(n,prod):
#         if n > 0:
#             return loop(n-1, b * prod)
#         else:
#             return prod
#     return loop(n,1)

# print(power3(2,5))

# code 4-16
# def power4(b,n):
#     prod = 1
#     while n >0:
#         n -= 1
#         prod *= b
#     return prod

# print(power4(2,5))

# code 4-17
# def power5(b,n):
#     if (n > 0 and n % 2 == 0):
#         return (b*b) ** (n /2)
#     elif (n>0 and n % 2 != 0):
#         return b * (b ** (n-1))
#     else:
#         return 1

# print(power5(2,5))

# def power5(b,n):
#     if n > 0:
#         if n % 2== 0:
#             return (b*b) ** (n /2)
#         else:
#             return b * (b ** (n-1))
#     else:
#         return 1

# print(power5(2,5)) 

# code 4-18 꼬리재귀
# def power6(b,n):
#     def loop(b,n,prod):
#         if n > 0:
#             if n % 2 == 0:
#                 return loop(b*b, n//2, prod)
#             else:
#                 return loop(b, n -1, prod * b)
#         else:
#             return prod
#     return loop(b,n,1)

# print(power6(2,5))

# code 4-19
# def power7(b,n):
#     prod  = 1
#     while n > 0:
#         if n % 2 == 0:
#             b *= b
#             n /= 2
#         else:
#              n -= 1
#              prod *= b
#     return prod

# print(power7(2,5))

# code 4-20
# def gcd(m,n):
#     if n != 0:
#         return gcd(n,m % n)
#     else:
#         return m

# print(gcd(48,18))


# code 4-21  **
# def gcd2(m,n):
#     while n != 0:
#         m,n = n, m%n
#     return m

# print(gcd2(48,18))







