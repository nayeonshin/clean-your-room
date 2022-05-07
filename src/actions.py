def inspect(*items):
    emojis = ["💌", "💐", "⌚"]

    indices_to_emojis = {
        i: emoji
        for i, emoji in enumerate(emojis)
    }

    for i, item in enumerate(items):
        print(indices_to_emojis[i], item)

    print()


def smell(flower):
    print(flower, "💨👃 ...*sniffs*")
