"""vowel count"""
text = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

for v in vowels:
    count = text.count(v)
    if count > 0:
        print(f"{v} : {count}")
