"""taxxi price calculate"""
def main():
    """start func"""
    distance = int(input())
    i = 0
    price = 0
    while i < distance:
        if i < 1:
            price += 35
        elif i < 10:
            price += 5
        else:
            price +=8
        i+=1
    print(price)

main()
