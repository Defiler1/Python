# code 5-33
# def ispalindrome(s):
#     if len(s) <= 1:
#         return True
#     elif s[0] != s[-1]:
#         return False
#     else:
#         return ispalindrome(s[1:-1])

# print(ispalindrome('abbaa'))

# code 5-34
# def ispalindrome(s):
#     return len(s) <= 1 or s[0] == s[-1] and ispalindrome(s[1:-1])

# print(ispalindrome('abba'))

# 5.2 삼각수(for 루프 버전)
# def trinum(n):
#     if n > 0:
#         return trinum(n -1) + n
#     else:
#         return 0

# def trinum(n):
#     r = 0
#     for i in range(n,0,-1):
#         r += i
#     return r

# print(trinum(6))

# 5.3 덧셈만 가지고 제곱 계산하기(for 루프 버전)
# def square(n):
#     def loop(n):
#         if n > 0:
#             return n + n - 1 + loop(n -1)
#         else:
#             return 0
#     return loop(abs(n))

# print(square(3))

# def square(n):
#     n = abs(n)
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i + i - 1
#     return sum

# print(square(3))

# 5.4 순열(for 루프 버전)
# def permutation(n,k):
#     if k > 0:
#         return permutation(n -1, k -1) * n
#     else:
#         return 1

# print(permutation(4,3))

# def permutation(n,k):
#     result = 1
#     for i in range(n,n-k,-1):
#         result = result * i 
#     return result

# print(permutation(4,3))

# 5.5 급수 계산(for 루프 버전)
import numbers


def sum_of_num_over_next(n):
    if n > 0:
        return sum_of_num_over_next(n -1) + n / (n + 1)
    else:
        return 0

# print(sum_of_num_over_next(5))

# n(i) = i / (i + 1)

def sum_of_num_over_next(n):
    result = 0
    for i in range(1,n + 1):
        result += i / (i + 1)
        return result

# print(sum_of_num_over_next(5))

# 5.6 윤년 출력 프로시저
def is_leap_year(year):
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0

def print_leap_year(yearfrom, yearto):
    print('Leap years between', yearfrom, 'and', yearto, ":")
    for i in range(yearfrom, yearto + 1):
        if is_leap_year(i):
            print(i)
        
# print_leap_year(1990,2004)

# 5-7 ISBN -10 코드 검증 (국제 표준 도서 번호)
# d9 = (d0 *1 + d1 *2 + d2*3 + d3*4 + d4*5 +d5*6 + d6*7 + d7*8 +d8*9) % 11

def isbn10(s):
    total = 0
    for i in range(1, 10):
        total = total + int(s[i -1]) * i
    last = total % 11
    if last == 10:
        return s[9] == 'X'
    else:
        return s[9] == str(last)

# print(isbn10('1413304540'))

# 5.8 문자열 빈칸 채우기
def fillwith_(str):
    new_sentence = ''
    for i in str:
        if i == ' ':
            new_sentence += '_'
        else:
            new_sentence += i 
    return new_sentence

# print(fillwith_('따스한 봄 나들이 갑시다.'))

# 5.9 모음 일련번호 매기기
# 영어 모음: a, e, i, o, u
def vowel_numbering(word):
    number = 1
    newword = ''
    for i in word:
        if i in ['a', 'e', 'i', 'o', 'u' 'A', 'E', 'I', 'O', 'U']:
            newword += str(number) 
            number += 1
        else:
            newword += i 
    return newword

# print(vowel_numbering('Massachuseettes'))

# 5.10 재귀 함수를 꼬리재귀, while 루프. for 루프 함수로 변환하기

# 재귀함수
# 원소가 짝수면 나누기 2 홀수면 곱하기 2
def updown(ns):
    if ns != []:
        if ns[0] % 2 == 0:
            return [ns[0]//2] + updown(ns[1:])
        else:
            return [ns[0]*2] + updown(ns[1:])
    else:
        return []
# Test
# print(updown([4,6,5,3,7,6,2,1,3,2]))

# 꼬리재귀
def updown2(ns):
    def loop(ns, result):
        if ns != []:
            if ns[0] % 2 == 0:
                return loop(ns[1:], result + [ns[0] // 2]) 
            else:
                return  loop(ns[1:], result + [ns[0] * 2])
        else:
            return result
    return loop(ns, [])

# print(updown2([4,6,5,3,7,6,2,1,3,2]))

# while 루프
def updown3(ns):
    result = []
    while ns != []:
        if ns[0] % 2 == 0:
            result += [ns[0] // 2]
        else:
            result += [ns[0] * 2]
        ns = ns[1:]
    return result

# print(updown3([4,6,5,3,7,6,2,1,3,2]))

# for 루프
def updown4(ns):
    result = []
    for i in ns:
        if i % 2 == 0:
            result += [i // 2] # result.append(i//2)
        else:
            result += [i * 2]
    return result


# print(updown4([4,6,5,3,7,6,2,1,3,2]))

# 5.11 부분 리스트

s = [1,2,3,4,5]

def drop_before(lst, index):
    if lst != [] and index > 0:
        return drop_before(lst[1:], index - 1)
    else:
        return lst

# print(drop_before(s, 2)) # s[2:]

def take_before(lst, index):
    if lst != [] and index > 0:
        return [lst[0]] + take_before(lst[1:], index -1)
    else:
        return []


# print(take_before(s, 2)) # s[:2]

def take_before2(lst, index):
    def loop(lst, index, result):
        if lst != [] and index > 0:
            result.append(lst[0])
            return loop(lst[1:], index -1, result)
        else:
            return result
    return loop(lst, index, [])

# print(take_before2(s, 2)) # s[:2]

def take_before3(lst, index):
    result = []
    while lst != [] and index > 0:
        result.append(lst[0])
        lst = lst[1:]
        index -= 1
    return result

# print(take_before3(s, 2)) # s[:2]

def sublist(s, low, high):
    if low < 0: low = 0
    if high < 0: high = 0
    if low <= high:
        return take_before(drop_before(s,low),high - low)
    else:
        return []

# print(sublist(s, 0, 3)) # [1,2,3]
