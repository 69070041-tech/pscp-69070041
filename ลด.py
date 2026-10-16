"""การเพิ่ม/ลด"""
a = float(input())
b = float(input())
c = float(input())

if a > b > c:
    print("decreasing")
elif a < b < c:
    print("increasing")
else:
    print("neither")
