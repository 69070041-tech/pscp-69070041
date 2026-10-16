"""card identifier"""
def main():
    """start function"""
    card = input().strip()

    rank_part = card[:-1].upper()
    suit_part = card[-1].upper()

    ranks = {
        'A': 'ace',
        'J': 'jack',
        'Q': 'queen',
        'K': 'king'
    }

    suits = {
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades',
        'C': 'clubs'
    }

    rank_name = ranks.get(rank_part, rank_part)
    suit_name = suits.get(suit_part, '')

    print(f"{rank_name} of {suit_name}")

main()
