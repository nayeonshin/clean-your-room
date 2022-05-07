class WashingMachine:
    def __init__(self):
        self.detergent = None
        self.clothes = {}

    def put(self, detergent, **kwargs):
        self.detergent = detergent
        self.clothes.update(kwargs)

    def start(self):
        pass

    def check_status(self):
        print()
        print("🧺")

        if self.clothes:
            for cycle, clothes in self.clothes.items():
                print(f"{cycle}:", clothes)
        else:
            print("(empty)")
