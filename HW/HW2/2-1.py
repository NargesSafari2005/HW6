
def paskal(L):
    l=[1]
    for i in range(len(L)):
        if i == len(L)-1:
            l.append(1)
        else:
            l.append(L[i]+L[i+1])
    L.clear()
    L.extend(l)
n = int(input())
if n==1:
    print(1)
elif n==2:
    print('1\n1 1')
else:
    print('1\n1 1')
    L=[1,1]
    for i in range(n-2):
        paskal(L)
        for j in L:
            print(j, end=' ')
        print()
