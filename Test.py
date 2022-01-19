print("Score Average Calculator")
number = input("How many classes? ")
while not (number.isdigit() and int(number) > 0):
    number = input("Enter a positive number: ")
print("The number of classes =", number)
total = 0
count = 0
while count < int(number):
    score = input("Enter your score: ")
    while not (score.isdigit() and 0 <= int(score) <= 100):
        score = input("Enter your score between 0 and 100: ")
    print("Your score =", score)
    total = total + int(score)
    count = count + 1
if count > 0:
    print("Your average score =", round(total/count,1))
else:
    print("Your average score = 0.0")






