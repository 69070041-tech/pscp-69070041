"""water state checker depend on temperature"""
temperature = int(input())
temperature_unit = input().lower()

if temperature_unit == "f":
    temperature -= 32
else:
    pass

if temperature <= 0:
    print("solid")
elif temperature >= 100:
    print("gas")
else:
    print("liquid")
