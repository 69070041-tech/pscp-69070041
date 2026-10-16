"""game score"""
def main():
    """Calculate game score"""
    n = int(input().strip())
    score = 0
    for _ in range(n):
        cmd = input().strip()
        if cmd == '+':
            score += 10
        elif cmd == '-':
            score -= 5
    print(score)

main()
