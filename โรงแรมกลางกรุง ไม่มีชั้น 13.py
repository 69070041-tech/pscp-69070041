"""Hotel Room Code Decrypter."""

def get_part1(digits):
    """Calculate the first part (floor number)."""
    floor_values = [9, 10, 11, 12, 14]
    for i, digit in enumerate(digits):
        if digit > 5:
            return floor_values[i]
    return 13


def get_part2(digits):
    """Calculate the second part (middle digit)."""
    if digits == digits[::-1]:
        if digits[0] + digits[4] > 5:
            return 1
        if digits[1] * digits[3] > 5:
            return 2
        return 0

    if digits[4] and (digits[0] // digits[4] > 5):
        return 1
    if digits[1] - digits[4] > 5:
        return 2
    return 0


def get_part3(digits):
    """Calculate the third part (last digit)."""
    if sum(digits) > 25:
        return 1

    total_prod = 1
    for digit in digits:
        total_prod *= digit

    if total_prod > 55:
        return 2
    return 0


def main():
    """Calculate and print the room number based on secret code N."""
    n_str = input().zfill(5)
    digits = [int(c) for c in n_str]

    part1 = get_part1(digits)
    part2 = get_part2(digits)
    part3 = get_part3(digits)

    print(f"{part1}{part2}{part3}")

main()
