import time

start = time.time()

def power6(b,n):
    def loop(b,n,prod):
        if n > 0:
            if n % 2 == 0:
                return loop(b*b, n//2, prod)
            else:
                return loop(b, n -1, prod * b)
        else:
            return prod
    return loop(b,n,1)

print(power6(2,100))

end = time.time()

print(end - start)