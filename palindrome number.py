def function(x):
    y = x
    a = 0
    while y > 0:
        a = a * 10 + y % 10
        y =y // 10
    return a == x

x = int(input('x ='))
print(function(x))