"""Module to analyze faulty tiles, spot counts, and calculate penalties."""


def analyze_row(row_data):
    """Calculate faulty tile count and total faulty spots in a single row."""
    faulty_tiles = sum(1 for spots in row_data if spots > 0)
    total_spots = sum(row_data)
    return faulty_tiles, total_spots


def main():
    """Read grid data, compute row/column defect stats, and print report."""
    first_line = input().split()
    grid_size = int(first_line[0])
    penalty_rate = float(first_line[1])

    col_faulty_tiles = [0] * grid_size
    col_total_spots = [0] * grid_size
    total_faulty_tiles = 0
    total_spots = 0

    for _ in range(grid_size):
        row_data = list(map(int, input().split()))
        row_tiles, row_spots = analyze_row(row_data)

        total_faulty_tiles += row_tiles
        total_spots += row_spots

        for col_idx, spots in enumerate(row_data):
            if spots > 0:
                col_faulty_tiles[col_idx] += 1
            col_total_spots[col_idx] += spots

        row_str = " ".join(map(str, row_data))
        print(f"{row_str} {row_tiles} {row_spots}")

    print(" ".join(map(str, col_faulty_tiles)))
    print(" ".join(map(str, col_total_spots)))

    total_penalty = total_spots * penalty_rate
    print(f"{total_faulty_tiles} {total_spots} {total_penalty:.2f}")


main()
