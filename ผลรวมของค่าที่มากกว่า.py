"""find the maximum value of two numbers and sum them up"""
def main():
    """start function"""
    n = int(input())

    max_values = []
    for _ in range(n):
        a = int(input())
        b = int(input())
        max_values.append(max(a, b))

    total_sum = sum(max_values)

    if n == 1:
        print(total_sum)
    else:
        expression = " + ".join(str(x) for x in max_values)
        print(f"{expression} = {total_sum}")


main()
