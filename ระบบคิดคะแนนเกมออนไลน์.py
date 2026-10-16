"""game score"""
def main():
    """start function"""
    base_score = int(input())
    bonus_score = int(input())
    day_played = int(input())

    if day_played > 3:
        total_score = int((base_score + bonus_score) * 1.5)
    else:
        total_score = int(base_score + bonus_score)

    if total_score >= 1500:
        rank = 5
    elif total_score >= 1000:
        rank = 4
    elif total_score >= 500:
        rank = 3
    elif total_score >= 200:
        rank = 2
    else:
        rank = 1
    if rank == 5 and day_played >= 7:
        code = "99"
    elif rank == 4 and bonus_score > 300:
        code = "88"
    else:
        code = "0"

    print(f"{total_score}")
    print(f"{rank}")
    print(f"{code}")

main()
