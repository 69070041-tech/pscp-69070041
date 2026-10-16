"""learning log ink collapse calculate"""
def main():
    """start func"""
    s,n = map(int, input().split())

    for _ in range(n):
        x, y = map(int, input().split())

        area = 3.1416 * (x*x + y*y)
        total = area/s

        ans = int(total)
        if total > ans:
            ans += 1

        print(ans)
main()
