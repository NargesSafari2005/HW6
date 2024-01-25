x = input().split()
y = int(input())
dict_x = {}
for j, a in enumerate(x):
    dict_x[int(a)] = j
dict_n = {}
for i in dict_x.keys():
    b = y - i
    if b in dict_x and b != i:
        m = dict_x[i] + dict_x[b]
        if (b,i) not in dict_n.keys():
            dict_n[(i,b)]=m
if not dict_n:
    print("Not Found!")
else:
    for j in sorted(dict_n.values()):
        print(j)