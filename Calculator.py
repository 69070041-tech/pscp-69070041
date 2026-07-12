"""wow"""
def main():
    """wow"""
    n = int(input())

    total_digit = 0

    for i in range(1, n + 1):
        total_digit += len(str(i))

    if n <= 1:
        total_press = 1
    else:
        total_press = total_digit + n
    print(total_press)

main()
