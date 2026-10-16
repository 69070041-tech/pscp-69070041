"""gee"""
def main():
    """yee"""
    n = int(input())

    first_val = int(input())
    minimum = first_val
    maximum = first_val
    total = first_val

    for _ in range(n - 1):
        val = int(input())
        total += val
        if val < minimum:
            minimum = val
        if val > maximum:
            maximum = val

    avg = total / n

    print(f"MIN: {minimum:.3f}")
    print(f"MAX: {maximum:.3f}")
    print(f"AVG: {avg:.3f}")

main()
