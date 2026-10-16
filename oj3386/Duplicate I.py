"""Module to find common student IDs across two groups."""


def main():
    """Read student IDs and print common ones from highest to lowest."""
    count_m = int(input())
    count_n = int(input())

    first_group = {input().strip() for _ in range(count_m)}
    second_group = {input().strip() for _ in range(count_n)}

    common_ids = sorted(first_group & second_group, reverse=True)

    if not common_ids:
        print("Nope")
        return

    for student_id in common_ids:
        print(student_id)


main()
