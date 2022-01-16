def fun(x):
    y =  x
    for n in range(2 , x):
        if  y % n == 0:
            return False
    if y != 1:
        return True

x = int(input('x ='))
print(fun(x))