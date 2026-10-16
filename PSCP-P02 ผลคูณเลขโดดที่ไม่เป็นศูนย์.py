"""Calculate product of non-zero digits."""
def main():
    """yeee"""
    digit = input().strip().strip("0")

    if not digit:
        print(0)
        return
    product = 1
    for char in digit:
        if char != "0":
            product*=int(char)

    print(product)

main()
