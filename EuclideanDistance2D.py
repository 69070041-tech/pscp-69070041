"""calculate something"""
import math

def main():
    """start func"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())

    calculate = math.sqrt(((q1-p1)**2)+((q2-p2)**2))

    print(calculate)

main()
