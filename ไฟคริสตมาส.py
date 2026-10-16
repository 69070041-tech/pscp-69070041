"""chrismas light color"""
def main():
    """start func"""
    start_char, n_str = input().split()
    n = int(n_str)

    colors = ["Red", "Green", "Blue"]
    color_map = {"R": 0, "G": 1, "B": 2}

    start_index = color_map[start_char]

    result = []
    for i in range(n):
        current_index = (start_index + i) % 3
        result.append(colors[current_index])

    print(" ".join(result))
main()
