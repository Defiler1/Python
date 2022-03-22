# 연습문제
# 카운트다운 타이머

# from time import sleep
# def countdown(n):
#     if n > 0:
#         print(n)
#         sleep(1)
#         countdown(n-1)
#     else:
#         print('Launch!')

# countdown(3)

# def countdown2(n):
#     while n > 0:
#         print(n)
#         sleep(1)
#         n -= 1
#     print('Launch!')

# countdown2(3)

# def countdown3(n):
#     if n > 0:
#         if n >= 10:
#             print(n)
#             sleep(1)
#             countdown3(n-1)
#         elif n < 10 and n > 0:
#             if n % 2 == 0:
#                 print('Launch Imminent!')
#                 sleep(1)
#                 countdown3(n -1)
#             else:
#                 print(n)
#                 sleep(1)
#                 countdown3(n -1)
#     else:
#         print('Launch!')

# countdown3(15)

# def countdown4(n):
#     while n > 0:
#         if n >= 10:
#             print(n)
#             sleep(1)
#             n -= 1
#         else:
#             if n % 2 == 0:
#                 print('Launch Imminent!')
#                 sleep(1)
#                 n -= 1
#             else:
#                 print(n)
#                 sleep(1)
#                 n -= 1
#     print('Launch!')

# countdown4(15)

# 팩토리얼

# def fac(n):
#     if n > 1:
#         return fac(n-1) * n
#     elif n == 1:
#         return 1
#     else:
#         return 0

# print(fac(5))

# 꼬리재귀
# def fac2(n):
#     def loop(n, result):
#         if n > 1:
#             return loop(n - 1, n * result)
#         else:
#             return result  
#     return loop(n, 1)

# print(fac2(5))
    
# def fac3(n):
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result

# print(fac3(5))

# 삼각수

# def trinum(n):
#     if n > 0:
#         return trinum(n -1) + n
#     else:
#         return 0

# print(trinum(6))

# 꼬리재귀
# def trinum2(n):
#     def loop(n, result):
#         if n > 0:
#             return loop(n -1, result + n)
#         else: 
#             return result
#     return loop(n, 0)

# print(trinum2(6))      

# def trinum3(n):
#     result = 0
#     while n > 0:
#         result += n
#         n -= 1
#     return result

# print(trinum3(6))

# 덧셈만 가지고 제곱 계산하기

# def square(n):
#     def loop(n):
#         if n > 0:
#             return n + n - 1 + loop(n -1)
#         else:
#             return 0
#     return loop(abs(n))

# print(square(-3))

# def square2(n):
#     def loop(n, result):
#         if n > 0:
#             return loop(n-1, result + n + n -1)
#         else:
#             return result
#     return loop(abs(n), 0)

# print(square2(6))

# def square3(n):
#     n = abs(n)
#     result =0
#     while n > 0:
#         result = result + n + n -1
#         n -= 1
#     return result

# print(square3(-6))
        

# 순열

# def permutation(n,k):
#     if k > 0:
#         return permutation(n -1, k -1) * n
#     else:
#         return 1

# print(permutation(4,4))

# def permutation2(n,k):
#     def loop(n,k,result):
#         if k > 0:
#             return loop(n-1, k-1, result * n)
#         else:
#             return  result
#     return loop(n,k,1)

# print(permutation2(4,4))

# def permutation3(n,k):
#     result = 1
#     while n > 0:
#         result *= n
#         k -= 1
#         n -= 1
#     return result

# print(permutation3(4,4))


# 급수계산

# def sum_of_num_over_next(n):
#     if n > 0:
#         return sum_of_num_over_next(n -1) + n / (n + 1)
#     else:
#         return 0
    
# print(sum_of_num_over_next(3))

# def sum_of_num_over_next2(n):
#     def loop(n, result):
#         if n > 0:
#             return loop(n -1, n / (n + 1) + result)
#         else:
#             return result
#     return loop(n, 0)

# print(sum_of_num_over_next2(3))

# def sum_of_num_over_next3(n):
#     result = 0
#     while n >0:
#         result = n / (n + 1) + result
#         n -= 1
#     return result

# print(sum_of_num_over_next3(3))


# def add_range(start, stop, step):
#     if start < stop:
#         return add_range(start + step, stop, step) + start
#     else:
#         return 0


# print(add_range(1,10,3))

# def add_range2(start, stop, step):
#     def loop(start,result):
#         if start < stop:
#             return loop(start + step, result + start)
#         else:
#             return result
#     return loop(start, 0)


# print(add_range2(1,10,3))


# def add_range3(start, stop, step):
#     result = 0
#     while start < stop:
#         result += start
#         start += step
#     return result

# print(add_range3(1,10,3))