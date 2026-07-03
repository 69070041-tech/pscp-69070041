"""frame word"""
def main():
    """start func"""
    word = str(input())

    check = len(word)
    frame = check + 2

    print("*"*frame)

    print(f"*{word}*")

    print("*"*frame)

main()
