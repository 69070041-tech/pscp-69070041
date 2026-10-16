"""Print a pattern of '*' and 'X' based on the input number."""
def main():
    """start function"""
    n = int(input().strip())
    result = []
    for i in range(1, n + 1):
        if not i % 5:
            result.append('X')
        else:
            result.append('*')
    print(''.join(result))

main()
