"""wow"""

def main():
    """start func"""
    power = int(input())
    check = power % 4

    if check == 1:
        print(7)
    elif check == 2:
        print(9)
    elif check == 3:
        print(3)
    else:
        print(1)

main()
