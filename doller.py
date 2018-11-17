from money import Money

class Doller(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Doller(self._amount * multiplier)

    def __eq__(self, other):
        return self.equals(other)

