"""elon musk"""
def main():
    """start func"""
    x_str, k = input().split()
    x = int(x_str)

    mid = x // 2

    for i in range(x):
        if k == "#":
            char = "#"
        else:
            dist_from_mid = abs(i - mid)
            char = chr(ord(k) + dist_from_mid)

        line = ""
        for j in range(x):
            if j in (i, x - 1 - i):
                line += char
            else:
                line += "-"

        print(line)

main()
