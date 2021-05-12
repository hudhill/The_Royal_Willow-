class Customer:
    def __init__(self, name, age):
        self.name = name
        self.wallet = 100
        self.age = age
        self.drunkenness = 0

    def get_wallet(self, name):
        return self.wallet

    def buy_a_drink(self, drink, pub, customer):
        if pub.check_age(customer) == True and pub.check_drunkenness(customer) == False:
            pub.till += drink.price
            self.wallet -= drink.price
            self.drunkenness += drink.alc_level
        else:
            return "Sorry buddy"

    def get_drunkenness(self):
        return self.drunkenness
    
    def buy_snack(self, food, pub):
        pub.till += food.price
        self.wallet -= food.price
        self.drunkenness -= food.rejuvenation_level 
