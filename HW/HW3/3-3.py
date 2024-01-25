import re

input = input()
input = re.sub(r' +', ' ', input.strip())
input = re.sub(r"\\n", "\n", input)
list = list(input)
arr = []
F = 0
for  j in list:
    if j == '@':
        arr.append(j)
        F  += 1
    elif  j == '#' and F > 0:
        F -= 1
    else:
        arr.append(j)
output = ''
for j in arr:
    output += j
print("Formatted Text: " , output)