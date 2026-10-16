"""vowel counter"""
def main():
    """start function"""
    word = input().lower()

    count = 0
    for char in word:
        if char in "aeiou":
            count += 1

    print(count)
main()
