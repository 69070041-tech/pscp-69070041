"""Module to validate Pad Thai ingredients and taste specifications."""


def collect_inputs(stop_token):
    """Collect unique inputs line by line until stop_token is entered."""
    items = set()
    while True:
        line = input().strip()
        if line == stop_token:
            break
        items.add(line)
    return items


def main():
    """Evaluate Pad Thai ingredients and flavors based on chef's criteria."""
    valid_ingredients = {
        "Pad Thai Sauce",
        "Tofu",
        "Pickle Turnip",
        "Shrimp",
        "Bean Sprouts",
        "Noodle",
        "Chives",
        "Lime",
        "Egg",
        "Oil",
        "Peanuts",
    }
    valid_tastes = {"Sweet", "Sour", "Salty"}

    user_ingredients = collect_inputs("Cook")
    user_tastes = collect_inputs("End")

    has_invalid_ingredient = not user_ingredients.issubset(valid_ingredients)
    has_all_ingredients = valid_ingredients.issubset(user_ingredients)

    if has_invalid_ingredient:
        print("This is not Pad Thai!!!")
    elif not has_all_ingredients:
        print("This is bad!")
    elif user_tastes == valid_tastes:
        print("Delicious!")
    else:
        print("Not Bad...")


main()
