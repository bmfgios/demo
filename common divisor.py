def function(x , y):
    if x > y:
        x , y = y , x
    for n in range(x , 1 , -1):
        if x % n == 0 and y % n == 0:
            return n

def fun(x , y):
    return x *  y // function(x , y)

x = int(input('x ='))
y = int(input('y ='))
print(function(x , y))
print(fun(x , y))