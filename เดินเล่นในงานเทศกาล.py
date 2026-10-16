"""find the final position and manhattan distance"""
def main():
    """start function"""

    text = input()
    x, y = 0, 0
    for char in text:
        if char == 'N':
            y += 1
        elif char == 'S':
            y -= 1
        elif char == 'E':
            x += 1
        elif char == 'W':
            x -= 1
    d = abs(x) + abs(y)
    print(f"{x} {y} {d}")


main()
