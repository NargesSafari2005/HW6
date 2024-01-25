import re

k = input()
k = re.sub(r' +', ' ', k.strip())
k = re.sub(r"\\n", "\n", k)
l = list(k)
i = []
F = 0
for  j in l:
    if j == '@':
        i.append(j)
        F  += 1
    elif  j == '#' and F > 0:
        F -= 1
    else:
        i.append(j)
R = ''
for j in i:
    R += j
print("Formatted Text: " , R)