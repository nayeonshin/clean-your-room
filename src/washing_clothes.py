class WashingMachine:
    def __init__(self):
        self.detergent = None
        self.clothes = {}
        self.is_clean = False

    def put(self, detergent, **kwargs):
        self.detergent = detergent
        self.clothes.update(kwargs)

    def start(self):
        print()
        print("Washing clothes... 🧼")
        self.is_clean = True

    def check_status(self):
        print()
        print("🧺")

        if self.clothes:
            status = "✨ CLEAN ✨" if self.is_clean else "💩 DIRTY 💩"
            print(status)
            for cycle, clothes in self.clothes.items():
                print(f"{cycle}:", clothes)
        else:
            print("(empty)")
