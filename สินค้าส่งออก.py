"""count even and odd numbers and find the sum of all numbers"""
def main():
    """start function"""
    n = int(input())

    total_sum = 0
    even_count = 0
    odd_count = 0

    for _ in range(n):
        x = int(input())
        total_sum += x
        if not x % 2:
            even_count += 1
        else:
            odd_count += 1

    print(f"SUM {total_sum}")
    print(f"EVEN {even_count}")
    print(f"ODD {odd_count}")

main()
