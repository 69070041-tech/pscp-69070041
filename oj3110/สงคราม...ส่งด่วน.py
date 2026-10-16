"""shipping fee calculate"""
def main():
    """start func"""
    start,finish = input().split()
    weight = float(input())

    routes = {
        ("BKK", "CNX"): (10, 30),
        ("CNX", "UBP"): (15, 40),
        ("UBP", "BKK"): (20, 40),
        ("BKK", "PKT"): (25, 50),
        ("PKT", "CNX"): (30, 60),
        ("UBP", "PKT"): (40, 70),
    }

    def calculate_fee(start, finish, weight):
        """fee calculate"""
        if (start,finish) in routes:
            base_fee, weight_fee = routes[(start,finish)]
            print(f"{(base_fee + (weight_fee * weight)):.2f}")
        else:
            print("Error")

    calculate_fee(start,finish,weight)

main()
