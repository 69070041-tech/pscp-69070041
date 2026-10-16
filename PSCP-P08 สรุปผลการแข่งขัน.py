"""yee"""
def main():
    """yeee"""
    yee = int(input())
    win_count = 0
    draw_count = 0
    lose_count = 0
    for _ in range(yee):
        match = input()
        if match == "WIN":
            win_count+=1
        elif match == "DRAW":
            draw_count+=1
        else:
            lose_count+=1
    print(win_count,draw_count,lose_count)
    print((win_count*3)+(draw_count))

main()
