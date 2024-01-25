from math import sqrt


def isPrime(x) :
    if x > 1:
        for i in range(2, sqrt(x)):
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False


a , b = input().split()
a = int(a)
b = int (b)
output = ""
if b >= a :
    output = "main order - amount: "
else :
    output = "reverse order - amount: "
    a,b = b,a

counter = 0

for i in range(a, b + 1):
    if isPrime(i):
        counter += 1

output += str(counter)
print(output)