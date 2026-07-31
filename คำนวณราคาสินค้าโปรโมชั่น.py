"""discount calculate"""
import math
pencil,book,color = map(int,input().split())

amount = pencil + book + color

pencil *= 25
book *= 40
color *= 55

if amount >= 3:
    print(math.floor((pencil + book + color)*90/100))
else:
    print((pencil + book + color))
