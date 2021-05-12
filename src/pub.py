class Pub:
    def __init__(self, name):
        self.name = name
        self.till = 0
        self.drinks = [ ]

    def get_till(self):
        return self.till

    def check_age(self, customer):
        can_buy = False
        if customer.age >= 21:
            can_buy = True
            return can_buy
        else:
            return "Sorry buddy"

    def check_drunkenness(self, customer):
        deny_service = False
        if customer.drunkenness > 10:
            deny_service = True
        return deny_service

