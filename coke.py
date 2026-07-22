"""yesn't"""
def solve():
    """yes"""
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())

    if not d:
        print(0)
        return

    if not b or c == a:
        print(d * a)
        return

    total_cost = 0
    coke_obtained = 0
    caps = 0

    while coke_obtained < d:
        if b == 1 and coke_obtained > 0:
            total_cost += c
            coke_obtained += 1
        elif caps >= b:
            caps -= b
            total_cost += c
            coke_obtained += 1
            caps += 1
        else:
            total_cost += a
            coke_obtained += 1
            caps += 1

    print(total_cost)

solve()
