"""yee"""
def main():
    """yee"""
    n = int(input())
    a = int(input())

    total_minutes = n * a

    if not total_minutes:
        print("No teaching")
    else:
        hours = total_minutes // 60
        minutes = total_minutes % 60

        if hours > 0 and minutes > 0:
            print(f"{hours} hours {minutes} minute")
        elif hours > 0:
            print(f"{hours} hours")
        else:
            print(f"{minutes} minute")

main()
