n = input().split()
n.sort(key=lambda i:int(i[1:]))
for i in n:
    print(i[0],end="")