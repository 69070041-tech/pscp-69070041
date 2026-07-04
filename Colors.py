"""color mixer"""
def main():
    """start func"""
    color1 = input().capitalize()
    color2 = input().capitalize()

    if color1 == "Red" and color2 == "Blue" or color1 == "Blue" and color2 == "Red":
        total_color = "Violet"
    elif color1 == "Red" and color2 == "Yellow" or color1 == "Yellow" and color2 == "Red":
        total_color = "Orange"
    elif color1 == "Blue" and color2 == "Yellow" or color1 == "Yellow" and color2 == "Blue":
        total_color = "Green"
    elif color1 == color2 and color1 in ('Red', 'Yellow', 'Blue'):
        total_color = color1
    else:
        total_color = "Error"

    print(total_color)

main()
