def method1():
    try:
        raise NameError()
        print(1)
    except SyntaxError:
        print(2)
    except Exception:
        print(3)
        raise NameError()
        print(4)
    except Exception:
        print(5)
    finally:
        print(6)
    print(7)



try:
    method1()
    print(8)
except Exception:
    print(9)

a, b= map(int, input('input ').split(","))
print(a, b)




