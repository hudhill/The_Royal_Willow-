class Food:
    def __init__(self, name, price, rejuvenation_level):
        self.name = name
        self.price = price
        self.rejuvenation_level = rejuvenation_level

    def rejuvenate(self):
        return self.rejuvenation_level 