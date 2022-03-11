import random

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
   for k in range(1,len(ns),1):  # 1,2,3,4,5,6
      for i in range(len(ns)-1): 
         if ns[i] > ns[i+1]:
            ns[i], ns[i+1] = ns[i+1], ns[i]
   return ns

# print(bubblesort([32,23,18,7,11,99,55]))
# print(bubblesort([71, 48, 3, 22, 56, 54, 7, 54, 61, 3, 10]))
# [7, 11, 18, 23, 32, 55, 99]

# 랜덤 리스트 만들기 함수
def build_ns():
   ns = []
   import math
   for i in range(math.floor(random.random() * 10)):
      a = math.floor(random.random() * 100)
      ns.append(a)
   return ns

# print(build_ns())

# code 8.6  기수 정렬
def radixsort(ds):
   if ds != []:
      length = len(ds[0])
      for i in range(length-1, -1, -1):   # 1,0
         distributed = [[] for _ in range(10)] # 이차원 배열 
         for j in ds:   # 정렬
            distributed[int(j[i])].append(j)
         ds = []                    # ds초기화
         for k in distributed:      # ds채우기
            # ds.append(k)          # distributed는 크기10 ds는 크기5 - out of range
            ds += k
      return ds
   else:
      return []

# print(radixsort(['33', '66', '92', '23', '79']))
# ds 요소는 모두 같은 길이


# 정답보드를 만들어 리턴
def initialize_board_4x4():
   row0 = [1,2,3,4]
   random.shuffle(row0)
   row1 = row0[2:4] + row0[0:2]
   row2 = [row0[1], row0[0], row0[3], row0[2]]
   row3 = row2[2:4] + row2[0:2]
   return [row0, row1, row2, row3]

# print(initialize_board_4x4())


# 가로줄 바꾸기
# 가로줄 0과 가로줄 1을 무작위로 바꾸고 가로줄 2와 3을 무작위로 바꿈
def shuffle_ribbons(board):
   top = board[:2]
   bottom = board[2:]
   random.shuffle(top)
   random.shuffle(bottom)
   return top + bottom



# 실습 8.6 가로세로 뒤집기
# 알고리즘 설명
# 가로세로를 뒤집어 저장할 보드를 초기화한다.
# 가로로 읽어서 세로로 차례로 붙여나간다.
# code 8.9
def transpose(board):
   transposed = []
   size = len(board)
   for _ in range(size):
      transposed.append([])
   for row in board:
      for i in range(size):
         transposed[i].append(row[i])
   return transposed

b1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# print(transpose(b1))


# 정답보드를 무작위로 하나 만들어 리턴
# code 8.10
def create_solution_board_4x4():
   board = initialize_board_4x4()   # 정답보드 만들기
   board = shuffle_ribbons(board)   # 랜덤하게 가로줄 바꾸기
   board = transpose(board)         # 가로세로 뒤집기
   board = shuffle_ribbons(board)   # 가로줄 바꾸기
   board = transpose(board)         # 가로세로 뒤집기
   return board


# 실습 8.7
# 복제한 정답보드와 빈칸의 개수를 인수로 받음
# 주어진 개수만큼 빈칸을 무작위로 만들어 리턴
def make_holes(board, no_of_holes):
   while no_of_holes > 0:
      i = random.randint(0,3) # 가로
      j = random.randint(0,3) # 세로
      if board[i][j] != 0:
         board[i][j] = 0
         no_of_holes -= 1
   return board



# 퍼즐보드를 실행창에 프린트하여 보여주는 프로시저
def show_board(board):
   for row in board:
      for entry in row:
         if entry == 0:
            print('.', end=' ')
         else:
            print(entry, end=' ')
      print()

