"""
Calculates total price by aggregating discount percentages first.
Fixes rounding precision issues.
"""

import math

def main():
    """start"""
    is_member = input().strip()
    n = int(input())

    total = 0.0
    for _ in range(n):
        total += float(input())

    if is_member == 'Y':
        discount = 5
    elif total >= 500:
        discount = 3
    else:
        discount = 0

    total_stang = round(total * 100)
    net_stang = math.ceil(total_stang * (100 - discount) / 100)

    ans = net_stang / 100

    print(f"{ans:.2f}")
main()
