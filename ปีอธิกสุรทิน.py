"""leap year checker by using conditi0on check no use module"""
year = int(input())

if year < 1582:
    is_leap = not year % 4
else:
    is_leap = (not year % 400) or (not year % 4 and bool(year % 100))

if is_leap:
    print("yes")
else:
    print("no")
