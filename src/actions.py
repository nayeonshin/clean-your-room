def inspect(*items):
    # TODO: use zip() instead of hard-coding the numbers
    indices_to_emojis = {1: "💌", 2: "💐", 3: "⌚"}

    for i, item in enumerate(items, 1):
        print(indices_to_emojis[i], item)
    print()


def smell(flower):
    print(flower, "💨👃 ...*sniffs*")
