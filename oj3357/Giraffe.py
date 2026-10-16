"""Module to count giraffes taller than their adjacent neighbors."""


def main():
    """Read giraffe heights and print count of strictly local peaks."""
    total = int(input())
    heights = [int(input()) for _ in range(total)]

    if total == 1:
        print(1)
        return

    count = 0
    for idx in range(total):
        is_peak = True
        if idx > 0 and heights[idx] <= heights[idx - 1]:
            is_peak = False
        if idx < total - 1 and heights[idx] <= heights[idx + 1]:
            is_peak = False

        if is_peak:
            count += 1

    print(count)


main()
