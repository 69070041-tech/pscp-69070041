"""/lotery compare to the win one"""
def main():
    """eiei"""
    prize_set, prize_num = input().split()
    buy_set, buy_num = input().split()

    is_set_match = prize_set == buy_set

    if is_set_match and prize_num == buy_num:
        print(1000000)

    elif not is_set_match and prize_num == buy_num:
        print(100000)

    elif is_set_match and buy_num[2:] == prize_num[2:]:
        print(2000)
    elif not is_set_match and buy_num[2:] == prize_num[2:]:
        print(200)

    elif is_set_match and buy_num[3:] == prize_num[3:]:
        print(1000)
    elif not is_set_match and buy_num[3:] == prize_num[3:]:
        print(100)

    elif is_set_match:
        print(20)

    else:
        print(0)

main()
