"""safe password"""
def main():
    """start func"""
    safe_char = str(input())
    safe_digit = int(input())

    if safe_char == "H" and safe_digit == 4567:
        print("safe unlocked")
    elif safe_char == "H" and safe_digit != 4567:
        print("safe locked - change digit")
    elif safe_char != "H" and safe_digit == 4567:
        print("safe locked - change char")
    else:
        print("safe locked")

main()
