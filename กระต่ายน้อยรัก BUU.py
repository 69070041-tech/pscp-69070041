"""Check rabbit screaming pattern for BUU."""

def main():
    """Process rabbit message and output pattern results."""
    text = input().strip()
    length = len(text)

    max_u = 0
    has_b = False
    first_b_idx = -1

    for i, char in enumerate(text):
        if char.upper() == "B":
            if not has_b:
                has_b = True
                first_b_idx = i

            u_count = 0
            j = i + 1
            while j < length and text[j].upper() == "U":
                u_count += 1
                j += 1

            if u_count >= 2 and u_count > max_u:
                max_u = u_count

    if max_u >= 2:
        print(f"Yes {max_u}")
    elif has_b:
        result = text[: first_b_idx + 1] + "U" * (length - first_b_idx - 1)
        print(result)
    else:
        result = ("BUU" * length)[:length]
        print(result)


main()
