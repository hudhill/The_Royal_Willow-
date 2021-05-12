import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Fred", 21)
        self.customer_2 = Customer("Samantha", 18)
        self.drink = Drink("Maitai", 6, 2)
        self.pub = Pub("The Royal Willow")
    
    def test_can_buy_drink(self):
        self.customer_1.buy_a_drink(self.drink, self.pub, self.customer_1)
        expected = 94
        actual = self.customer_1.get_wallet(self.customer_1.name)
        self.assertEqual(expected, actual)
        expected = 6
        actual = self.pub.get_till()
        self.assertEqual(expected, actual)

    def test_cannot_buy_drink(self):
        self.customer_2.buy_a_drink(self.drink, self.pub, self.customer_2)
        self.assertEqual("Sorry buddy", self.pub.check_age(self.customer_2))

    def test_can_get_drunk(self):
        self.customer_1.buy_a_drink(self.drink, self.pub, self.customer_1)
        self.assertEqual(2, self.customer_1.get_drunkenness())
