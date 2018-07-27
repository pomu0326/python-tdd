class Doller:
    __amount = 0

    def __init__(self, amount):
        self.__amount = amount

    def times(self, multiplier):
        return Doller(self.__amount * multiplier)

    def equals(self, object):
        return self.__amount == object.__amount

    def __eq__(self, other):
        return self.equals(other)

