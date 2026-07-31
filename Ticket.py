"""Ticket price setup"""
def main():
    """start func"""
    age, day = map(str,input().split())

    if int(age) < 5 :
        price = 0
    elif int(age) <= 18:
        price = 100
    else:
        price = 150

    if day == "Wed":
        print(int(price/2))
    else:
        print(price)

main()
