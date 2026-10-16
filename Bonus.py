"""bonus calculate by role"""
def main():
    """start func"""
    role, work_time, money = input().split()
    role = role.upper()
    work_time = float(work_time)
    money = float(money)

    # Set base bonus amount
    if role == "M":
        base = 1500
        # Boundary logic handling
        if work_time <= 5:
            rate = 0.06
        elif work_time <= 10:
            rate = 0.08
        else:  # >= 10
            rate = 0.10

    elif role == "B":
        base = 1000
        if work_time <= 5:
            rate = 0.05
        elif work_time <= 10:
            rate = 0.06
        else:  # >= 10
            rate = 0.07

    else:  # "G"
        base = 500
        if work_time <= 5:
            rate = 0.04
        elif work_time <= 10:
            rate = 0.05
        else:  # >= 10
            rate = 0.06

    total_bonus = (money * rate) + base
    print(int(total_bonus))

main()
