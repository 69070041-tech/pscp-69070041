"""Module to sort 2D points by sum ascending and y-coordinate descending."""


def get_sort_key(point):
    """Return sort key using sum of coordinates and negated y-value."""
    pos_x, pos_y = point
    return pos_x + pos_y, -pos_y


def solve_test_case():
    """Read points for one test case and print sorted coordinates."""
    point_count = int(input())
    points = []

    for _ in range(point_count):
        pos_x, pos_y = [int(val) for val in input().split()]
        points.append((pos_x, pos_y))

    points.sort(key=get_sort_key)

    for pos_x, pos_y in points:
        print(f"{pos_x} {pos_y}")


def main():
    """Process all test cases for point sorting."""
    test_cases = int(input())
    for _ in range(test_cases):
        solve_test_case()


main()
