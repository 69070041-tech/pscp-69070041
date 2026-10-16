"""Flower bed band calculator."""

def main():
    """Find the band index for the N-th planted flower."""
    l_val, n_val = map(int, input().split())

    k = 1
    while True:
        total_cells = (k * l_val) * (k * l_val + 1) // 2
        if total_cells >= n_val:
            print(k)
            break
        k += 1

main()
