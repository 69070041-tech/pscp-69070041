"""filter scope in barier checker"""
r, x, y = map(int,input().split())

if x**2 + y**2 < r**2:
    print("IN")
elif x**2 + y**2 > r**2:
    print("OUT")
else:
    print("ON")
