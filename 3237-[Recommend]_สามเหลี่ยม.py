"""
Program to print a right-angled triangle with outline '0' and filled with '1'.
Height is determined by integer input n.
"""

n = int(input())

for i in range(n):
    for j in range(i + 1):
        if not j or j == i or i == n - 1:
            print("0",  end="")
        else:
            print("1",end="")
    print()
