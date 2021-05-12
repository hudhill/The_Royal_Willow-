import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub
from src.food import Food

class TestFood(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Fred", 21)
        self.customer_2 = Customer("Samantha", 18)
        self.drink = Drink("Maitai", 6, 2)
        self.drink_2 = Drink("Blackout Bucket", 20, 11)
        self.pub = Pub("The Royal Willow")
        self.apple = Food("Apple", 1, 2)
        self.crisps = Food("Crisps", 3, 1.5)

    def test_rejuvenate(self):
        self.customer_1.drunkenness = 6
        self.customer_1.buy_snack(self.crisps, self.pub)
        self.assertEqual(4.5, self.customer_1.get_drunkenness())