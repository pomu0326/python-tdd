from abc import *

class Money(metaclass=ABCMeta):
    def __init__(self, amount):
        self._amount = amount

    @abstractmethod
    def times(self, multiplier): pass

    def equals(self, object):
        if not isinstance(object, Money):
            return False
        if not type(self) == type(object):
            return False
        return self._amount == object._amount

    def doller(amount):
        return Doller(amount)

    def franc(amount):
        return Franc(amount)

class Doller(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier) -> Money:
        return Doller(self._amount * multiplier)

    def __eq__(self, other):
        return self.equals(other)

class Franc(Money):

    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier) -> Money:
        return Franc(self._amount * multiplier)

    def __eq__(self, other):
        return self.equals(other)
