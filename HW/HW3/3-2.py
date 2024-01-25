import re
a = int(input())
b = set()
while  a != 0 :
    c = input()
    a -= 1
    d = re.findall("@[A-Za-z]+.[A-Za-z]+",c)
    for i in d:
        b.add(i[1:])
b = list(b)
b.sort()
for i in b:
    print(i)