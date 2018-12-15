from abc import *

class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self) -> str:
        return self._currency

    def equals(self, object):
        if not isinstance(object, Money):
            return False
        return self._amount == object._amount \
               and self._currency == object._currency

    def doller(amount):
        return Money(amount, "USD")

    def franc(amount):
        return Money(amount, "CHF")

    def __repr__(self):
        return "{} {}".format(self._amount, self._currency)

    def __eq__(self, other):
        return self.equals(other)

