def isleapyear(year):
    if (year >= 0) :
        return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))
    else:
        return None

print(isleapyear(0))
print(isleapyear(1))
print(isleapyear(4))