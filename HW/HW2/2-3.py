def sum_of_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

def base_of_conversion(x, y):
    list = []
    while x != 0:
        list.append(x % y)
        x = x // y
    list.reverse()
    t = ''
    for i in list:
        t = t + str(i)
    t = int(t)
    return t


L = []
flag = 0
while True:
    n, y = map(int, input().split())
    if n == -1 and y == -1:
        break
    elif 2 <= y <= 9:
        converted_n = base_of_conversion(sum_of_divisors(n), y)
        L.append(converted_n)
    else:
        flag = 1

if flag == 1:
    print("invalid base!")
else:
    print(sum(L))