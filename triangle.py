n = int(input('请输入行数: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j>n:
            print('*',end='')
        else:
            print(' ',end='')
    print()

for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print()