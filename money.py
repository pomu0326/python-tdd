class Money:
    def __init__(self, amount):
        self._amount = amount

    def equals(self, object):
        return self._amount == object._amount


