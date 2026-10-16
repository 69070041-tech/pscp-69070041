"""IJUGDE URL difficulty checker."""


def get_tail(url, prefix):
    """Get tail of url after prefix."""
    tail = ""
    idx = 0
    for char in url:
        if idx >= len(prefix):
            tail += char
        idx += 1
    return tail


def is_valid_tail_len(tail):
    """Check whether tail has a valid length."""
    if len(tail) == 4 and not tail.endswith("/"):
        return True
    if len(tail) == 5 and tail.endswith("/"):
        return True
    return False


def get_star(tail):
    """Return star rating if digits are valid."""
    count = 0
    star = ""
    for char in tail:
        if not count:
            star = char
            if char not in "0123":
                return ""
        elif count < 4:
            if char not in "0123456789":
                return ""
        count += 1
    return star


def main():
    """Main function."""
    url = input()
    prefix = "https://ijudge.it.kmitl.ac.th/problems/"

    if url.startswith(prefix):
        tail = get_tail(url, prefix)
        if is_valid_tail_len(tail):
            star = get_star(tail)
            if star:
                print(f"{star} STAR")
                return

    print("INVALID")


main()
