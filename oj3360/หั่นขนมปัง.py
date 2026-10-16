"""Module to find the two largest bread pieces after cutting."""


def get_widths(cuts, total_length):
    """Compute segments between cut lines and boundaries."""
    points = [0] + cuts + [total_length]
    return [points[idx] - points[idx - 1] for idx in range(1, len(points))]


def main():
    """Read cuts and print top two bread piece areas."""
    width, height, _, _ = [int(val) for val in input().split()]
    x_cuts = [int(val) for val in input().split()]
    y_cuts = [int(val) for val in input().split()]

    widths = sorted(get_widths(x_cuts, width), reverse=True)
    heights = sorted(get_widths(y_cuts, height), reverse=True)

    w1 = widths[0]
    w2 = widths[1] if len(widths) > 1 else 0
    h1 = heights[0]
    h2 = heights[1] if len(heights) > 1 else 0

    max_area = w1 * h1
    second_area = max(w1 * h2, w2 * h1)

    print(f"{max_area} {second_area}")


main()
