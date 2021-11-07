def rot(num):
    num = num.replace('6', '9', 1)
    return num

num = input()

print(rot(num))
