"""combine 2 code equal 9"""
def main():
    """start func"""
    n = int(input())

    code1 = str(input().strip())
    code2 = (input().strip())

    mistake_match = 0

    for i in range(n):
        digit1 = int(code1[i:i+1])
        digit2 = int(code2[i:i+1])

        if digit1 + digit2 != 9:
            mistake_match += 1

    if not mistake_match:
        print("YES")
    else:
        print(f"NO {mistake_match}")
main()
