"""Module to shorten a sequence of numbers into ranges."""


def format_range(start, end):
    """Format single number or start-end range string."""
    if start == end:
        return str(start)
    return f"{start}-{end}"


def main():
    """Read numbers until -1 and print shortened ranges."""
    first = int(input())
    if first == -1:
        return

    ranges = []
    start = first
    prev = first

    while True:
        num = int(input())
        if num == -1:
            ranges.append(format_range(start, prev))
            break

        if num == prev + 1:
            prev = num
        else:
            ranges.append(format_range(start, prev))
            start = num
            prev = num

    print(", ".join(ranges))


main()
