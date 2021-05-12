class Drink:
    def __init__(self, name, price, alc_level):
        self.name = name
        self.price = price
        self.alc_level = alc_level

    def get_alc_level(self):
        return self.alc_level
