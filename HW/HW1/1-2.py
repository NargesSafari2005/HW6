a = int(input())
b = int(input())
sum_of_a_b = int(input())
while a:
    x = (a & b) << 1
    y = a ^ b
    a = x
    b = y
print(b)
if b != sum_of_a_b :
    print("NO")
else:
    print("YES")