"""Check triangle type."""


def is_valid_shape(side_a, side_b, side_c):
    """Check if three sides can form a triangle."""
    cond_a = side_a + side_b > side_c
    cond_b = side_a + side_c > side_b
    cond_c = side_b + side_c > side_a
    return cond_a and cond_b and cond_c


def is_right_angle(side_a, side_b, side_c):
    """Check if triangle has a right angle."""
    sq_a = side_a * side_a
    sq_b = side_b * side_b
    sq_c = side_c * side_c
    cond_c = sq_a + sq_b == sq_c
    cond_b = sq_a + sq_c == sq_b
    cond_a = sq_b + sq_c == sq_a
    return cond_c or cond_b or cond_a


def get_triangle_type(side_a, side_b, side_c):
    """Find triangle type."""
    if not is_valid_shape(side_a, side_b, side_c):
        return "NOT A TRIANGLE"
    if side_a == side_b == side_c:
        return "EQUILATERAL"
    if is_right_angle(side_a, side_b, side_c):
        return "RIGHT TRIANGLE"
    if side_a == side_b or side_b == side_c or side_a == side_c:
        return "ISOSCELES"
    return "SCALENE"


def main():
    """Main function."""
    side_a = int(input())
    side_b = int(input())
    side_c = int(input())
    result = get_triangle_type(side_a, side_b, side_c)
    print(result)


main()
