"""ของขวัญและขโมย"""
def main():
    """start function"""
    n, k, t = map(int, input().split())

    current = 1
    count = 1

    while True:
        if current == t:
            break

        current = (current + k - 1) % n + 1

        if current == 1:
            break

        count += 1

    print(count)

main()
