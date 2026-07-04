"""d"""
def main():
    """d"""
    x = int(input())
    y = int(input())
    a = float(input())
    z = float(input())
    
    pro_group = z // x
    left_pp = z % x
    pro_cost = (pro_group * y) * a
    normal_cost = left_pp * a
    total = (pro_cost + normal_cost)

    print(total)

main()
