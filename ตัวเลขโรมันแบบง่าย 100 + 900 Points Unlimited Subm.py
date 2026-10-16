"""number change to roman number"""
roman_num = {
    1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
    6: "VI", 7: "VII", 8: "VIII", 9: "IX"
}

n = int(input())

if n < 0:
    print("Error : Please input positive number")
elif not n or n > 9:
    print("Error : Out of range")
else:
    print(roman_num[n])
