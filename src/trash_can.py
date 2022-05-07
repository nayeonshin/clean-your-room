class TrashCan:
    def __init__(self):
        self.trash_can = set()

    def put(self, *trash):
        for item in trash:
            self.trash_can.add(item)

    def check(self):
        print()
        print("🗑️:")

        if self.trash_can:
            for item in self.trash_can:
                print(item)
        else:
            print("(empty)")

    def empty(self):
        self.trash_can.clear()
