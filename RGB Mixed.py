"""yee"""
def main():
    """yee"""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())

    r_new = (r1 + r2) // 2
    g_new = (g1 + g2) // 2
    b_new = (b1 + b2) // 2

    print(f"{r_new} {g_new} {b_new}")

main()
