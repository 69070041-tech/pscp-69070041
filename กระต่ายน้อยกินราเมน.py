"""คำนวณราคาราเมน"""
def main():
    """ramen price calculator"""
    size, ramen_type = input().split()

    topping_input = input().split()

    ramen_prices = (
        ('S', 'R', 60),
        ('S', 'T', 80),
        ('M', 'R', 80),
        ('M', 'T', 100),
        ('L', 'R', 100),
        ('L', 'T', 120)
    )

    topping_prices = (
        ('P', 15),
        ('E', 10),
        ('N', 0)
    )

    total_price = 0
    for item in ramen_prices:
        if item[0] == size and item[1] == ramen_type:
            total_price = item[2]
            break

    topping_code = topping_input[0]
    if topping_code != 'N':
        count = int(topping_input[1])
        for item in topping_prices:
            if item[0] == topping_code:
                total_price += item[1] * count
                break

    print(total_price)

main()
