"""Calculate parking fees at Suvarnabhumi Airport."""

def time_to_minutes(t_str):
    """Convert time string in 'H.M' format to total minutes."""
    if t_str.count('.') != 1:
        return None

    parts = t_str.split('.')
    h_str, m_str = parts[0], parts[1]

    if not (h_str.isdigit() and m_str.isdigit()):
        return None

    h = int(h_str)

    if len(m_str) == 1:
        m_str = m_str + '0'

    if len(m_str) > 2:
        return None

    m = int(m_str)

    if h < 0 or h > 23 or m < 0 or m > 59:
        return None

    return h * 60 + m

def main():
    """Suvarnabhumi Airport Parking Fee Calculator"""
    entry_str = input().strip()
    exit_str = input().strip()

    entry_min = time_to_minutes(entry_str)
    exit_min = time_to_minutes(exit_str)

    if entry_min is None or exit_min is None or exit_min < entry_min:
        print("ERROR")
        return

    diff = exit_min - entry_min

    if diff > 1440:
        print("ERROR")
    elif diff <= 15:
        print("FREE")
    else:
        hours = (diff + 59) // 60

        if hours == 1:
            print(25)
        elif hours == 2:
            print(50)
        elif hours == 3:
            print(80)
        elif hours == 4:
            print(110)
        elif hours == 5:
            print(145)
        elif hours == 6:
            print(180)
        elif 7 <= hours <= 24:
            print(250)
        else:
            print("ERROR")

main()
