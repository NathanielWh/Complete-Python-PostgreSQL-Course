class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return "%.{}f".format(self.places) % self.number


class Currency(Decimal):
    def __init__(self, symbol, number, places):
        super().__init__(number, places)
        self.symbol = symbol

    def __repr__(self):
        return "{}{}".format(self.symbol, super().__repr__())


print(Decimal(11.2131, 3))

print(Currency("$", 15.6789, 3))

test = Decimal(2,4)

print(test)

foo = Currency("$", 12 , 2)


test.__repr__()


