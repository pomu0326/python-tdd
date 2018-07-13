import unittest
from doller import Doller

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Doller(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertTrue(Doller(5).equals(Doller(5)))
        self.assertFalse(Doller(5).equals(Doller(6)))

if __name__ == "__main__":
    unittest.main()

