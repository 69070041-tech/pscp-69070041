"""Cipher text using Caesar cipher with a given shift value."""
def main():
    """Caesar cipher text"""
    text = input().strip()
    k = int(input().strip())

    result = []
    for char in text:
        if 'a' <= char <= 'z':
            new_char = chr((ord(char) - ord('a') + k) % 26 + ord('a'))
            result.append(new_char)
        else:
            result.append(char)

    print(''.join(result))

main()
