"""car taxs calculate"""
year = int(input())
cc = int(input())

if year <= 1990:
    if cc <= 1500:
        print("1250")
    elif cc <= 2000:
        print("1400")
    else:
        print("2000")
elif 1990 < year <= 1999:
    if cc <= 1500:
        print("1100")
    elif cc <= 2000:
        print("1300")
    else:
        print("1700")
else:
    if cc <= 1500:
        print("1000")
    elif cc <= 2000:
        print("1200")
    else:
        print("1500")
