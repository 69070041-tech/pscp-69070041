"""back ward number"""
n = int(input())

while n >= 0:
    if n % 10:
        n-=1
    elif not n % 10:
        print(n,end=" ")

        n-=1
