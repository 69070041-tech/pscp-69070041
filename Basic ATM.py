"""atm bank diposit calculator"""
amount = int(input())

if amount < 100 or amount > 20000 or amount % 100:
    print("ERROR")
else:
    bill1000 = amount // 1000
    remain = amount % 1000
    bill500 = remain // 500
    remain = remain % 500
    bill100 = remain // 100

    if bill1000 > 0:
        print("1000 =", bill1000)
    if bill500 > 0:
        print("500 =", bill500)
    if bill100 > 0:
        print("100 =", bill100)
