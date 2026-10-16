"""yee"""
def main():
    """yeee"""
    N, L = map(int, input().split())
    H = list(map(int, input().split()))
    A = list(map(int, input().split()))

    for p in A:
        if p == 1:
            print(0)
            continue

        tallest = max(H[:p-1])
        chair = tallest - H[p-1] + 1

        if chair < 0:
            chair = 0

        print(chair)
main()
