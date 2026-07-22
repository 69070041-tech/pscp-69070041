"""Temperature unit converter"""


def main():
    """start func"""
    temperature = float(input())
    unit_in = input().strip().lower()
    unit_out = input().strip().lower()

    if unit_in == "k":
        celsius = temperature - 273.15
    elif unit_in == "f":
        celsius = (temperature - 32) * (5 / 9)
    elif unit_in == "r":
        celsius = (temperature - 491.67) * (5 / 9)
    else:
        celsius = temperature

    if unit_out == "k":
        result = celsius + 273.15
    elif unit_out == "f":
        result = (celsius * (9 / 5)) + 32
    elif unit_out == "r":
        result = (celsius + 273.15) * (9 / 5)
    else:
        result = celsius

    print(f"{result:.2f}")


main()
