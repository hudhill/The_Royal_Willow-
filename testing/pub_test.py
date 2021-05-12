import unittest

from src.customer import Customer
from src.drink import Drink
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Fred", 21)
        self.customer_2 = Customer("Samantha", 18)
        self.drink = Drink("Maitai", 6, 2)
        self.drink_2 = Drink("Blackout Bucket", 20, 11)
        self.pub = Pub("The Royal Willow")

    def test_give_service(self):
        self.customer_1.buy_a_drink(self.drink, self.pub, self.customer_1)
        self.assertEqual(False, self.pub.check_drunkenness(self.customer_1))

    def test_deny_service(self):
        self.customer_1.buy_a_drink(self.drink_2, self.pub, self.customer_1)
        self.assertEqual(True, self.pub.check_drunkenness(self.customer_1))