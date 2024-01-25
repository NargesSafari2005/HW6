a = int(input())
b = int(input())
n = int(input())
for j in range(0,n):
    i = int(input())
    if (i <=31):
        if (a & (1<<i)):
            print('yes')
        else:
            print('no')
    else:
        if (b & (1<<(i-32))):
            print('yes')
        else:
            print('no')