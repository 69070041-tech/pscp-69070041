import sys

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    if n <= 0:
        return
    first = int(next(it))
    lo = first
    hi = first
    total = first
    cnt = 1
    while cnt < n:
        v = int(next(it))
        if v < lo:
            lo = v
        if v > hi:
            hi = v
        total += v
        cnt += 1
    avg = total / n
    sys.stdout.write("MIN: %.3f\n" % lo)
    sys.stdout.write("MAX: %.3f\n" % hi)
    sys.stdout.write("AVG: %.3f" % avg)

if __name__ == "__main__":
    main()
