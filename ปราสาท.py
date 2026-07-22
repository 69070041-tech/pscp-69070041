"""yee"""
num = int(input().strip())

r = 1

while r * r < num:
    r+=1

c = num - (r - 1) **2

if not c % 2:
    print(2 * r - 3)
else:
    print(2 * r - 2)
