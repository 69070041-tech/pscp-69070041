"""Movie ticket queue management system."""


def main():
    """Process movie ticket purchases based on age and remaining seats."""
    try:
        seats_input = input().strip()
        if not seats_input:
            return
        seats = int(seats_input)
    except EOFError:
        return

    while seats > 0:
        try:
            line = input().strip()
            if not line:
                break
            parts = line.split()
            if len(parts) < 2:
                break
            age = int(parts[0])
            qty = int(parts[1])
        except (EOFError, ValueError):
            break

        if age < 15:
            print(-1)
        elif qty > seats:
            print(-2)
        else:
            if 15 <= age <= 22:
                price = 120
            elif age >= 60:
                price = 75
            else:
                price = 150

            total = price * qty
            seats -= qty
            print(f"{total} {seats}")


main()
