"""number checker"""
i = 0
num = []

while i < 3:
    num.append(int(input()))
    i+=1

num.sort()
print(num[0])
