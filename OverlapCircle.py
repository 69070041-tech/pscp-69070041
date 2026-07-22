"""Hi"""

x1 = int(input())
y1 = int(input())
r1 = int(input())
x2 = int(input())
y2 = int(input())
r2 = int(input())

distance_square = (x2 - x1)**2 + (y2 - y1)**2

r_sum = (r1 + r2)**2

if distance_square <= r_sum:
    print("overlapping")

else:
    print("no overlapping")
