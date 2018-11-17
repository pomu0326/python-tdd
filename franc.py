from money import Money

class Franc(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        return self.equals(other)

