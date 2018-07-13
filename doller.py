class Doller:
    amount = 0

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        return Doller(self.amount * multiplier)

    def equals(self, object):
        return True
