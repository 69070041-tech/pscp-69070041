"""inflation"""
n = float(input())
k = int(input())

satang = int(n * 100)

for _ in range(k):
    added_satang = (satang * 381) // 10000
    satang += added_satang

baht = satang // 100
st = satang % 100

print(f"{baht}.{st:02d}")
