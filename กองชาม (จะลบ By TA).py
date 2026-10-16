"""yee"""
def main():
    """yee"""
    try:
        line = input().strip()
        if not line:
            return
        n = int(line)
    except EOFError:
        return

    counts = {}
    read_count = 0

    while read_count < n:
        try:
            inp = input()
            if not inp:
                continue
            for val in map(int, inp.split()):
                counts[val] = counts.get(val, 0) + 1
                read_count += 1
        except EOFError:
            break

    if counts:
        print(max(counts.values()))


main()
