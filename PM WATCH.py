"""PM2.5 daily air monitor."""


def main():
    """Read PM2.5 data and display stats."""
    total_days = int(input())

    over_count = 0
    peak_val = 0
    best_run = 0
    best_start = 0

    curr_run = 0
    curr_start = 0

    for day in range(1, total_days + 1):
        val = int(input())
        if val > peak_val:
            peak_val = val

        if val > 50:
            over_count += 1
            if not curr_run:
                curr_start = day
            curr_run += 1
            if curr_run >= best_run:
                best_run = curr_run
                best_start = curr_start
        else:
            curr_run = 0
            curr_start = 0

    print(f"OVER = {over_count}")
    print(f"PEAK = {peak_val}")
    print(f"STREAK = {best_run}")
    print(f"START = {best_start}")


main()
