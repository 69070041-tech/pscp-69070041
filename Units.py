"""Thai unit converter."""


def get_factor(unit):
    """Return factor in niu."""
    if unit == "NIU":
        return 1.0
    if unit == "KUEP":
        return 12.0
    if unit == "SOK":
        return 24.0
    if unit == "WA":
        return 96.0
    return 1920.0


def main():
    """Main function."""
    val = float(input())
    target = input()
    source = input()

    val_in_niu = val * get_factor(source)
    ans = val_in_niu / get_factor(target)

    print(f"{ans:.4f}")


main()
