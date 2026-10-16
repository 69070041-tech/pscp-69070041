"""วิเคราะห์ยอดขายร้านกาแฟ"""
def main():
    """start function"""
    n = int(input())

    total_sales = 0
    max_sales = -1
    min_sales = 1001

    for _ in range(n):
        x = int(input())
        total_sales += x
        if x > max_sales:
            max_sales = x
        if x < min_sales:
            min_sales = x

    avg_sales = total_sales / n

    print(total_sales)
    print(max_sales)
    print(min_sales)
    print(f"{avg_sales:.1f}")

main()
