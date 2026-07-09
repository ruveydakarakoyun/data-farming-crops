class Rice:
    def __init__(self):
        self.grains = 0

    def water(self):
        self.grains += 5

    def ripe(self):
        return self.grains >= 15

    def transplant(self):
        self.grains += 10
