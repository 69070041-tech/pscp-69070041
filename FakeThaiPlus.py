"""Thai Chuay Thai aid check."""


def get_tier(card, income):
    """Find tier and base aid."""
    if card == "Y" or income <= 15000:
        return "GOLD", 3000
    if income <= 30000:
        return "SILVER", 1500
    return "", 0


def main():
    """Run program."""
    name = input()
    age = int(input())
    income = int(input())
    card = input()
    dependents = int(input())

    if age < 18:
        print(f"{name} NOT ELIGIBLE")
        return

    tier, amount = get_tier(card, income)
    if not tier:
        print(f"{name} NOT ELIGIBLE")
        return

    if dependents >= 3:
        amount += 500

    print(f"{name} {tier} {amount}")


main()
