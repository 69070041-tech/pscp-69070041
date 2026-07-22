"""coin checker"""
money = int(input())

coin_type = [10,5,2,1]

for coin in coin_type:
    count = money // coin

    money = money % coin

    print(f"{coin} = {count}")
