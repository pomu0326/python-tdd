from abc import *

class Expression(metaclass=ABCMeta):
    @abstractmethod
    def reduce(self, to): pass

class Bank:
    def reduce(self, source, to):
        return source.reduce(to)


class Sum(Expression):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Money(Expression):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend):
        # return Money(self._amount + addend._amount, self._currency)
        return Sum(self, addend)

    def currency(self) -> str:
        return self._currency

    def equals(self, object):
        if not isinstance(object, Money):
            return False
        return self._amount == object._amount \
               and self._currency == object._currency

    def reduce(self, to):
        return self

    def doller(amount):
        return Money(amount, "USD")

    def franc(amount):
        return Money(amount, "CHF")

    def __repr__(self):
        return "{} {}".format(self._amount, self._currency)

    def __eq__(self, other):
        return self.equals(other)

