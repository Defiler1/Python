import random

# # Begginer - 숫자 10개 채워줌 빈칸 6개
# # Intermediate - 숫자 8개 채워줌 빈칸 8개
# # Advanced - 숫자 6개 채워줌 빈칸 10개

# row = int(input('Row#(1,2,3,4): '))
# column = int(input('Column#(1,2,3,4): '))
# number = int(input('Number(1,2,3,4): '))

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



# 정답보드를 무작위로 하나 만들어 리턴
# code 8.10
def create_solution_board_4x4():
   board = initialize_board_4x4()   # 정답보드 만들기
   board = shuffle_ribbons(board)   # 랜덤하게 가로줄 바꾸기
   board = transpose(board)         # 가로세로 뒤집기
   board = shuffle_ribbons(board)   # 가로줄 바꾸기
   board = transpose(board)         # 가로세로 뒤집기
   return board


# 정답보드를 복제
def copy_board(board):
   board_clone = []
   for row in board:
      board_clone.append(row[:])
   return board_clone

# print(copy_board([[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]))


# Begginer - 숫자 10개 채워줌 빈칸 6개
# Intermediate - 숫자 8개 채워줌 빈칸 8개
# Advanced - 숫자 6개 채워줌 빈칸 10개
# 레벨을 입력받아 빈칸의 개수 정하기
def get_level():
   level = input('난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요 : ')
   while level not in ('1','2','3'):
      level = input('난이도(초급 1 중급 2 고급 3)를 숫자로 입력해주세요 : ')
   if level == '1':
      return 6
   elif level == '2':
      return 8
   else:
      return 10


# 4. puzzle_board에 no_of_holes만큼 무작위로 선택하여 0으로 채우기
def make_holes(board, no_of_holes):
   while no_of_holes > 0:
      i = random.randint(0,3) # 가로
      j = random.randint(0,3) # 세로
      if board[i][j] != 0:
         board[i][j] = 0
         no_of_holes -= 1
   return board


# 퍼즐보드 실행창에 보여줌
def show_board(board):
   for row in board:
      for entry in row:
         if entry == 0:
            print('.', end=' ')
         else:
            print(entry, end=' ')
      print()


def get_integer(message, i, j):
   number = input(message)
   while not (number.isdigit() and i <= int(number) <= j):
      # str.isdigit() -> 문자열이 숫자로만 구성되 있는지 확인하는 메서드
      # number를 올바르지 않게 입력했을때 while문 실행
      number = input(message)
   return int(number)


def sudoku_mini():
   solution_board = create_solution_board_4x4()    # 정답보드 생성
   puzzle_board = copy_board(solution_board)       # 정답보드 카피
   no_of_holes = get_level()                       # 레벨 입력 받아서 빈칸 개수 결정
   puzzle_board = make_holes(puzzle_board, no_of_holes)  # 퍼즐보드 생성
   show_board(puzzle_board)
   while no_of_holes > 0:
      i = get_integer('가로줄번호(1~4): ',1,4) - 1
      j = get_integer('세로줄번호(1~4): ',1,4) - 1
      if puzzle_board[i][j] != 0:
         print('빈칸이 아닙니다.')
         continue
      n = get_integer('숫자(1~4): ',1,4)
      if n == solution_board[i][j]:
         puzzle_board[i][j] = solution_board[i][j]
         show_board(puzzle_board)
         no_of_holes -= 1
      else:
         print(n,'가(이) 아닙니다. 다시 해보세요.')
   print('잘 하셨습니다. 또 들려주세요.')

sudoku_mini()