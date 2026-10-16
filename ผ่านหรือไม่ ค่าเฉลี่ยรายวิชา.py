"""calculate the average score and check if all scores are passed"""
def main():
    """start function"""
    n = int(input())

    total_score = 0
    is_all_passed = True

    for _ in range(n):
        score = int(input())
        total_score += score
        if score < 50:
            is_all_passed = False

    avg_score = total_score / n

    print(f"{avg_score:.1f}")

    if is_all_passed and avg_score >= 60.0:
        print("PASS")
    else:
        print("FAIL")


main()
