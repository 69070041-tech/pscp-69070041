"""yeee"""
def main():
    """yee"""
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except EOFError:
        return

    tokens = []
    while len(tokens) < n:
        try:
            inp = input()
            if inp:
                tokens.extend(inp.split())
        except EOFError:
            break

    heavy_count = 0
    light_count = 0

    for token in tokens:
        if int(token) > 18:
            heavy_count += 1
        else:
            light_count += 1

    if light_count >= heavy_count - 1:
        print(n)
    else:
        print(2 * heavy_count - 1)


main()
