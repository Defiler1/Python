# code 8.1
def code8_1():
   couples = []
   for c in ['a', 'b']:
      for n in range(3):
         couple = (c,n)
         couples.append(couple)

# [('a',0),('a',1),('a',2),('b',0),('b',1),('b',2)]


# code 8.2
def digit_art_horizontal(n):
   for i in range(n):
      for j in range(n):
         print(j + 1, end='')
      print()

# digit_art_horizontal(7)
# 1234567
# 1234567
# 1234567
# 1234567
# 1234567
# 1234567
# 1234567

# 실습 8.1 가로 변형
def digit_art_horizontal_left_down(n):
   for i in range(1, n + 1):
      for j in range(i):
         print(j + 1, end = '')
      print()

# digit_art_horizontal_left_down(7)
# 1
# 12
# 123
# 1234
# 12345
# 123456
# 1234567


def digit_art_horizontal_left_up(n):
   for i in range(n):  
      for j in range(n-i):
         print(j + 1, end='')
      print()

# digit_art_horizontal_left_up(7)

# code 8.3
def digit_art_vertical(n):
   for i in range(n):
      for j in range(n):
         print(i + 1, end='')
      print()

# digit_art_vertical(7)
# 1111111
# 2222222
# 3333333
# 4444444
# 5555555
# 6666666
# 7777777


# 실습 8.2 세로 변형
def digit_art_vertical_right_down(n):
   for i in range(n):
      for j in range(n):
         if n - 1 - i > j:
            print(' ', end='')
         else:  
            print(i+1, end='')
      print()

# digit_art_vertical_right_down(7)
#       1
#      22
#     333
#    4444
#   55555
#  666666
# 7777777

# n = 7
# for i in range(n):
#    for j in range(n):
#       if j != n - 1 - i:
#          print(' ',end='')
#       else:
#          print(i+1,end='')
#    print()

#       1
#      2
#     3
#    4
#   5
#  6
# 7

# code 8.4
def digit_art_horizontal_alternate(n):
   for i in range(n):      # [0,1,2,3,4,5,6]
      for j in range(n):   # [0,1,2,3,4,5,6]
         if i % 2 == 0:    # [0,2,4,6]
            print(j+1, end='')
         else:             # [1,3,5]
            print(n-j, end='')
      print()

# digit_art_horizontal_alternate(7)

# print(j+1, end='') [0,2,4,6]
# print(n-j, end='') [1,3,5]
# 1234567
# 7654321
# 1234567
# 7654321
# 1234567
# 7654321
# 1234567

# 실습 8.3 세로 방향 바꾸기
def digit_art_vertical_alternate(n):
   for i in range(n):
      for j in range(n):
         if j % 2 == 0:
            print(i+1, end='')
         else:
            print(n-i,end='')
      print()

# digit_art_vertical_alternate(7)
# 1717171
# 2626262
# 3535353
# 4444444
# 5353535
# 6262626
# 7171717


# code 8.5     bubble sort 버블 정렬
def bubblesort(ns):
   for k in range(1,len(ns),1):
      for i in range(len(ns)-1):
         if ns[i] > ns[i+1]:
            ns[i], ns[i+1] = ns[i+1], ns[i]
   return ns

print(bubblesort([32,23,18,7,11,99,55]))
# [7, 11, 18, 23, 32, 55, 99]