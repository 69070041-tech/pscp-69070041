"""Pizza party calculator."""


def main():
    """Calculate pizza orders."""
    people = int(input())
    each = int(input())
    per_tray = int(input())

    needed = people * each
    trays = (needed + per_tray - 1) // per_tray
    leftover = (trays * per_tray) - needed

    print(needed)
    print(trays)
    print(leftover)


main()
