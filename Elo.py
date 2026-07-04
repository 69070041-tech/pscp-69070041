"""elo winrate"""
def main():
    """start func"""
    ra = int(input())
    rb = int(input())
    player = str(input().capitalize())

    rating_a = (rb - ra) / 400
    rating_b = (ra - rb) / 400

    ea = 1 / (1 + 10 ** rating_a)
    eb = 1 / (1 + 10 ** rating_b)

    if player == "A":
        print(f"{ea:.2f}")
    else:
        print(f"{eb:.2f}")

main()
