class Doller:
    amount = 0

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount = self.amount * 2
