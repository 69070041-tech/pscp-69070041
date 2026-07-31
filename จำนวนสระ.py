"""vowel checker in the input"""
times = int(input())
i = 0
for _ in range(times):
    char = input().strip().lower()

    if char in "aeiou":
        i+=1
    _+=1


print(i)
