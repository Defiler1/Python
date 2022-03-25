# 8.1 구구단 출력

def gugudan_garo():
   for i in range(2,10):
      for j in range(2,10):
         print(i, 'x', j, '=', i * j, end='\t')
      print()

# gugudan_garo()

def  gugudan_sero():
   for i in range(2,10):
      for j in range(2,10):
         print(str(j), 'x', str(i), '=', str(i * j).rjust(2), end='\t')
      print()

# gugudan_sero()


# 8.2 ASCII Sharp 아트
def ascii_art(n):
   for i in range(n):
      for j in range(n):
         print('#', end=' ')
      print()

# ascii_art(5)

# 인수는 홀수만 들어옴
def ascii_art_cross(n):
   for i in range(n):
      for j in range(n):
         if i == (n//2):
            print('#', end=' ')
         else:
            if j == (n//2):
               print('#',end=' ')
            else:
               print(' ',end=' ')
      print()

# ascii_art_cross(7)

# if문 사용빈도 줄인 버전
def ascii_art_cross2(n):
   for i in range(n):
      for j in range(n):
         if i == (n//2) or j == (n//2):
            print('#', end=' ')
         else:
            print(' ',end=' ')
      print()


# ascii_art_cross2(5)

# ***
def ascii_art_X(n):
   for i in range(n):
      for j in range(n):
         if i == j or i + j == n - 1:
            print('#',end=' ')
         else:
            print(' ',end=' ')
      print()
      
# ascii_art_X(5)


def ascii_art_square(n):
   for i in range(n):
      for j in range(n):
         if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('#',end=' ')
         else:
            print(' ',end=' ')
      print()

# ascii_art_square(5)


def ascii_art_diamond(n):
   mid = n // 2
   for i in range(n):
      for j in range(n):
         if i + j == mid or  abs(i-j) == mid or i+j == n + mid -1:
            print('#',end=' ')
         else:
            print(' ',end=' ')
      print()

# ascii_art_diamond(5)


# p.405