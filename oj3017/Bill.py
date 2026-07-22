"""bill auto calculate"""
def main() :
    """start func"""
    price = float(input())

    service_charge = price * 10 / 100

    if service_charge <= 50.00 :
        plus_service_charge = price + 50.00
    elif service_charge >= 1000.00:
        plus_service_charge = price + 1000.00
    else:
        plus_service_charge = price + service_charge

    vat = plus_service_charge * 7 / 100
    plus_vat = plus_service_charge + vat

    print(f"{plus_vat:.2f}")
main()
