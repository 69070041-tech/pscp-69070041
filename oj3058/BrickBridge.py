"""brick used calculator"""
a = int(input())
b = int(input())
goal = int(input())

big_used = min(b, goal // 5)

remaining = goal - (big_used * 5)

if a >= remaining:
    print(remaining)
else:
    print("-1")
