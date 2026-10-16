"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())

n = 0

for i in range(a,b+1):
    if i % d == r:
        n+=1
print(n)
