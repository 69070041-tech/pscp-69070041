"""yeeeeeeeeeeeeeeeeeeee
    thai help thai 60 40 
    government money eiei
"""
wallet = int(input())
d = int(input())

month_quota = 1000
successful_items = 0
total_gov_paid = 0

day_idx = 0
while day_idx < d:
    day_quota = 200
    k = int(input())

    item_idx = 0
    while item_idx < k:
        price = int(input())

        user_share = (price * 40) // 100

        gov_share = price - user_share

        if gov_share > day_quota:
            gov_share = day_quota

        if gov_share > month_quota:
            gov_share = month_quota

        actual_pay = price - gov_share

        if wallet >= actual_pay:
            wallet -= actual_pay
            day_quota -= gov_share
            month_quota -= gov_share
            total_gov_paid += gov_share
            successful_items += 1

        item_idx += 1

    day_idx += 1

print(successful_items)
print(wallet)
print(total_gov_paid)
