def main():
    item_counts = {}
    grocery_items = get_grocery_list()
    for item in grocery_items:

# - item_counts.get(item, 0) returns the current count if 'item' exists, or 0 if it doesn't
# - adding 1 increases the count by one
# - then we store the updated count back in counts[item]

        item_counts[item] = item_counts.get(item, 0) + 1

    for item in sorted(item_counts):
        print(item_counts[item], item)

def get_grocery_list():
    items = []

    while True:
        try:
            user_input = input().upper()
            items.append(user_input)

        except KeyboardInterrupt:
            print()
            return items
        except EOFError:
            print()
            return items

main()