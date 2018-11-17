class Money:
    def __init__(self, amount):
        self._amount = amount

    def equals(self, object):
        if not isinstance(object, Money):
            return False
        return self._amount == object._amount
