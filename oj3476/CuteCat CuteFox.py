"""Module to organize and count cats and foxes in a flock using dictionaries."""

def parse_dict_entry(raw_text):
    """Extract key-value pair from JSON-like dictionary string."""
    clean_text = raw_text.strip().strip("{}")
    key_part, val_part = clean_text.split(":", 1)
    name = key_part.strip().strip("\"'")
    tag = val_part.strip().strip("\"'")
    return name, tag

def main():
    """Read animal entries, ensure defaults, and display sorted catalog."""
    total_entries = int(input().strip())
    animals = {}

    for _ in range(total_entries):
        name, tag = parse_dict_entry(input())
        animals[name] = tag

    # ตรวจสอบค่าเริ่มต้น Cat01 และ Fox01
    has_cat01 = any(tag == "Cat01" for tag in animals.values()) or "Garfield" in animals
    has_fox01 = any(tag == "Fox01" for tag in animals.values()) or "Fubuki" in animals

    if not has_cat01:
        animals["Garfield"] = "Cat01"
    if not has_fox01:
        animals["Fubuki"] = "Fox01"

    cats = []
    foxes = []

    for name, tag in animals.items():
        if tag.startswith("Cat"):
            num = int(tag.replace("Cat", ""))
            cats.append((num, tag, name))
        elif tag.startswith("Fox"):
            num = int(tag.replace("Fox", ""))
            foxes.append((num, tag, name))

    # เรียงลำดับตามตัวเลข
    cats.sort(key=lambda item: item[0])
    foxes.sort(key=lambda item: item[0])

    # แสดงผลจำนวน
    print(f"Cat : {len(cats)}")
    print(f"Fox : {len(foxes)}")

    # แสดงผลรายชื่อ
    for _, tag, name in cats:
        print(f"{name} : {tag}")
    for _, tag, name in foxes:
        print(f"{name} : {tag}")

main()
