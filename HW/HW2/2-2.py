def inputs():
    nums = []
    while True:
        n = input()
        if n == "end":
            break
        else:
            num = int(n)
            nums.append(num)
    return nums
def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def lcd(x, y):
    return x * y / gcd(x, y)
command = input()
if (command == "sum"):
    nums = inputs()
    print(sum(nums))
elif (command == "average"):
    nums = inputs()
    average = sum(nums) / len(nums)
    print(round(average, 2))
elif (command == "max"):
    nums = inputs()
    print(max(nums))
elif (command == "min"):
    nums = inputs()
    print(min(nums))
elif (command == "gcd"):
    nums = inputs()
    a = nums[0]
    for i in range(1, len(nums)):
        a = gcd(a, nums[i])
    print(a)
elif (command == "lcd"):
    nums = inputs()
    a = nums[0]
    for i in range(1, len(nums)):
        a = lcd(a, nums[i])
    print(int(a))
else:
    print("Invalid command")