"""asdad"""

number = input().strip()
operator = input().strip()

reversed_number = number[::-1]

num1 = int(number)
num2 = int(reversed_number)

if operator == "+":
    FINAL = num1 + num2
elif operator == "*":
    FINAL = num1 * num2
else:
    FINAL = 0

print(f"{num1} {operator} {num2} = {FINAL}")
