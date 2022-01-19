def smaller(x,y):
    if x < y:
        return x
    else:
        return y

def smallest(x,y,z):
    if x < y:
        if x < z:
            return x
        else:
            return z
    else:
        if y < z:
            return y
        else:
            return z

def median(x,y,z):
    one = smallest(x,y,z)
    if one == x:
        return smaller(y,z)
    elif one == y:
        return smaller(x,z)
    else:
        return smaller(x,y)

print(median(1,3,5))
print(median(3,5,1))
print(median(3,3,3))
print(median(3,5,3))
print(median(3,5,5))