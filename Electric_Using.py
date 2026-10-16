"""yeee"""
def main():
    """yeee"""
    n = int(input().strip())

    units = n
    cost = 0

    t1 = min(units, 10)
    cost += t1 * 5
    units -= t1

    if units > 0:
        t2 = min(units, 40)
        cost += t2 * 7
        units -= t2

    if units > 0:
        t3 = min(units, 50)
        cost += t3 * 10
        units -= t3

    if units > 0:
        t4 = min(units, 100)
        cost += t4 * 12
        units -= t4

    if units > 0:
        cost += units * 15

    total = cost * 1.07 + n * 0.5
    ans = int(total * 10 + 0.5) / 10

    print(f"{ans:.1f}")

main()
