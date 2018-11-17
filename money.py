from abc import *

class Money(metaclass=ABCMeta):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @abstractmethod
    def times(self, multiplier): pass

    def currency(self) -> str:
        return self._currency

    def equals(self, object):
        if not isinstance(object, Money):
            return False
        if not type(self) == type(object):
            return False
        return self._amount == object._amount

    def doller(amount):
        return Doller(amount, "USD")

    def franc(amount):
        return Franc(amount, "CHF")

class Doller(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier) -> Money:
        return Money.doller(self._amount * multiplier)

    def __eq__(self, other):
        return self.equals(other)

class Franc(Money):

    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier) -> Money:
        return Money.franc(self._amount * multiplier)


    def __eq__(self, other):
        return self.equals(other)