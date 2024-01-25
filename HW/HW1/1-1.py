y = int(input())
x = int(input())
output = 0
res = x ^ y
while res :
    output += 1
    res &= res -1
print(output)