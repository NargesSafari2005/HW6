n = int(input())
move = 0
l = []
for i in range(n):
    l.append('.')
L = []
L.extend([l.copy()])
i = 0
j = 0
L[0][0] = '*'
while move != 'END':
    move = input()
    if move == 'B':
        L.extend([l.copy()])
        j += 1
    elif move == 'R' and i != n-1:
        i += 1
    elif move == 'L' and i != 0:
        i -= 1
    L[j][i] = '*'
for t in range(len(L)):
    print(*L[t])
if i != n-1:
    print("There's no way out!")