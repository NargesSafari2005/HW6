
def paskal(input):
    arr=[1]
    for i in range(len(L)):
        if i == len(L)-1:
            arr.append(1)
        else:
            arr.append(L[i]+L[i+1])
    input.clear()
    input.extend(l)
n = int(input())
if n==1:
    print(1)
elif n==2:
    print('1\n1 1')
else:
    print('1\n1 1')
    numbers=[1,1]
    for i in range(n-2):
        paskal(numbers)
        for j in numbers:
            print(j, end=' ')
        print()
