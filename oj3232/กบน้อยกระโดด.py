"""Jumping Frog"""
def main():

    """start function"""
    x, y = map(int, input().split())

    current_jump = x
    total_distance = 0
    jump_count = 0

    while current_jump > 0:
        total_distance += current_jump
        jump_count += 1

        if total_distance >= y:
            print(jump_count)
            return

        current_jump -= 2

    print(-1)

main()
