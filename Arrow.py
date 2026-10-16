"""Arrow"""
def main():
    """Arrow"""
    s = input().strip()
    n = int(input())
    for idx, direction in enumerate(s):
        if direction == 'R':
            for i in range(n):
                print('  ' * i + '*' * (n - i))
            for i in range(n - 2, -1, -1):
                print('  ' * i + '*' * (n - i))
        else:
            for i in range(n):
                print(' ' * (n - 1 - i) + '*' * (n - i))
            for i in range(n - 2, -1, -1):
                print(' ' * (n - 1 - i) + '*' * (n - i))
        if idx != len(s) - 1:
            print()
main()
