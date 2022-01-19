print('Score Average Calculator')
c = input('How many classes? ')

while not (c.isdigit() and int(c) > 0):
    c = input('Enter a position number: ')

print('The number of classes =', c)
sum = 0

for i in range(int(c)):
    s = input('Enter your score: ')

    while not (s.isdigit() and 0 <= int(s) <= 100):
        s = input('Enter your score between 0 and 100: ')

    print('Your score =', s)
    sum += int(s)

print('Your average score =', sum / int(c))