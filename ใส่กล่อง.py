"""yee"""
def main():
    """yee"""
    try:
        line = input().strip()
        if not line:
            return
        w, l, m, n = map(int, line.split())
    except EOFError:
        return

    ans = min((l % a) * (w % a) for a in range(m, n + 1))
    print(ans)


main()
