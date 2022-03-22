# code 5-1
# from time import sleep
# def countdown(n):
#     while n > 0:
#         print(n)
#         sleep(1)
#         n -= 1
#     print('Launch!')

# countdown(5)

# code 5-2
# def countdown2(n):
#     for i in range(n,0,-1):
#         print(i)
#         sleep(1)
#     print('lauch!')

# countdown2(5)

# code 5-3
# def sigma(n):
#     sum=0
#     while n > 0:
#         n, sum = n-1, n+sum
#     return sum

# print(sigma(5))

# code 5-4
# def sigma2(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum += i
#     return sum

# print(sigma2(5))

# code 5-5
# def sumrange(m,n):
#     sum = 0
#     while m <= n:
#         sum += m
#         m += 1
#     return sum

# print(sumrange(4,5))

# code 5-6
# def sumrange2(m,n):
#     sum = 0
#     for i in range(m, n +1):
#         sum += i
#     return sum

# print(sumrange2(4,5))

# code 5-7
# def fac(n):
#     ans = 1
#     while n > 0:
#         n,  ans= n-1, ans*n
#     return ans

# print(fac(5))

# code 5-8
# def fac2(n):
#     ans = 1
#     for i in range(n,0,-1):
#         ans *= i
#     return ans

# print(fac2(5))

# code 5-9
# def power(b,n):
#     prod =1
#     while n > 0:
#         prod *= b
#         n -= 1
#     return prod

# print(power(2,5))

# code 5-10
# def power2(b,n):
#     prod =1
#     for i in range(n):
#         prod *= b
#     return prod

# print(power2(2,5))

# code 5-11 **
# def select_sort(xs):
#     if xs != []:
#         smallest = min(xs)
#         xs.remove(smallest)
#         return [smallest] + select_sort(xs)
#     else:
#         return []

# print(select_sort([3,5,4,2]))

# code 5-13
# def select_sort2(xs):
#     def loop(xs, ss):
#         if xs != []:
#             smallest = min(xs)
#             xs.remove(smallest)
#             return loop(xs, ss + [smallest])
#         else:
#             return ss
#     return loop(xs, [])

# print(select_sort2([3,5,4,2]))

# code 5-14
# def select_sort3(xs):
#     def loop(xs, ss):
#         if xs != []:
#             smallest = min(xs)
#             xs.remove(smallest)
#             ss.append(smallest)
#             return loop(xs, ss)
#         else:
#             return ss
#     return loop(xs, [])

# print(select_sort3([3,5,4,2]))

# code 5-15
# def select_sort4(xs):
#     ss = []
#     while xs != []:
#         smallest = min(xs)
#         xs.remove(smallest)
#         ss.append(smallest)
#     return ss

# print(select_sort3([3,5,4,2]))

# code 5-16
# def insertion_sort(xs):
#     if xs != []:
#         return insert(xs[0],insertion_sort(xs[1:]))
#     else:
#         return []

# print(insertion_sort([3,5,4,2]))

# code 5-17
# def insert(x, ss):
#     if ss != []:
#         if x <= ss[0]:
#             return [x] + ss
#         else:
#             return [ss[0]] + insert(x,ss[1:])
#     else:
#         return [x]

# print(insert(4,[1,2,3,5,6]))

# code 5-18
# def insert2(x, ss):
#     def loop(ss, result):
#         if ss != []:
#             if x <= ss[0]:
#                 result.append(x)
#                 return result + ss
#             else: 
#                 result.append(ss[0])
#                 return loop(ss[1:],result)
#         else:
#             result.append(x)
#             return result
#     return loop(ss, [])

# print(insert2(4, [1,2,3,5,6]))


# code 5-19
# def insert3(x, ss):
#     result = []
#     while ss != []:
#         if x <= ss[0]:
#             result.append(x)
#             return result + ss
#         else:
#             result.append(ss[0])
#             ss = ss[1:]
#     result.append(x)
#     return result

# print(insert3(4, [1,2,3,5,6]))

# code 5-20
# def insert(x, ss):
#     if ss != []:
#         if x <= ss[0]:
#             return [x] + ss
#         else:
#             return [ss[0]] + insert(x,ss[1:])
#     else:
#         return [x]

# def insertion_sort(xs):
#     if xs != []:
#         return insert(xs[0],insertion_sort(xs[1:]))
#     else:
#         return []    
# print(insertion_sort([3,5,4,2]))

# code 5-21
# def insertion_sort2(xs):
#     def loop(xs, result):
#         if xs != []:
#             return loop(xs[1:], insert(xs[0],result))
#         else:
#             return result
#     return loop(xs,[])

# print(insertion_sort2([3,5,4,2]))

# code 5-22
# def insertion_sort3(xs):
#     result = []
#     while xs != []:
#         xs, result = xs[1:], insert(xs[0], result)
#     return result

# print(insertion_sort3([3,5,4,2]))

# code 5-23
# def insertion_sort4(xs):
#     result = []
#     for i in xs:
#         result = insert(i, result)
#     return result

# def insertion_sort4(xs):
#     result = []
#     for i in range(len(xs)):
#         xs, result = xs[1:], insert(xs[0], result)
#         return result

# print(insertion_sort4([3,5,4,2]))

# code 5-24
def merge_sort(xs):
    if len(xs) > 1:
        mid = len(xs) //2
        return merge(merge_sort(xs[:mid]), merge_sort(xs[mid:]))
    else:
        return xs

# code 5-25
def merge(left, right):
    if not(left== [] or right ==[]):
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:],right)
        else:
            return [right[0]]+merge(left, right[1:])
    else:
        return left + right

# print(merge([18,23,32],[7,11,55,99]))

# code 5-26
def merge2(left, right):
    def loop(left, right, result):
        if not(left == [] or right == []):
            if left[0] <= right[0]:
                result.append(left[0])
                return loop(left[1:],right,result)
            else:
                result.append(right[0])
                return loop(left, right[1:], result)
        else:
            return result + left + right
    return loop(left, right, [])

# print(merge2([18,23,32],[7,11,55,99]))

# code5-27
def merge3(left, right):
    result = []
    while not(left == [] or right == []):
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    return result + left + right

# print(merge3([18,23,32],[7,11,55,99]))
def partition(pivot, xs):
    if xs != []:
        left, right = partition(pivot, xs[1:])
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []

# code 5-28 ***
def quicksort(xs):
    if len(xs) > 1:
        pivot = xs[0]
        (left, right) = partition(pivot, xs[1:])
        return quicksort(left) + [pivot] + quicksort(right)
    else:
        return xs

# print(quicksort([2,67,3,4,1]))

# code 5-29
def partition(pivot, xs):
    if xs != []:
        left, right = partition(pivot, xs[1:])
        if xs[0] <= pivot:
            left.append(xs[0])
        else:
            right.append(xs[0])
        return left, right
    else:
        return [], []

# print(partition(2,[67,3,4,1]))

# code 5-30
def partition2(pivot, xs):
    def loop(xs, ls, rs):
        if xs != []:
            if xs[0] <= pivot:
                ls.append(xs[0])
            else:
                rs.append(xs[0])
            return loop(xs[1:],ls,rs)
        else:
            return ls, rs
    return loop(xs, [], [])

# print(partition2(2,[67,3,4,1]))

# code 5-31
def partition3(pivot, xs):
    ls, rs = [], []
    while xs != []:
        if xs[0] <= pivot:
            ls.append(xs[0])
        else:
            rs.append(xs[0])
        xs = xs[1:]
    return ls, rs

# print(partition3(2, [67,3,4,1]))

# code 5-32
def partition4(pivot, xs):
    ls, rs = [], []
    for i in xs:
        if i <= pivot:
            ls.append(i)
        else:
            rs.append(i)
    return ls, rs

# print(partition4(2, [97,3,4,1]))

