import unittest
from franc import Franc
from money import Money, Doller

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.doller(5).equals(Money.doller(5)))
        self.assertFalse(Money.doller(5).equals(Money.doller(6)))
        self.assertTrue(Franc(5).equals(Franc(5)))
        self.assertFalse(Franc(5).equals(Franc(6)))
        self.assertFalse(Franc(5).equals(Money.doller(5)))

if __name__ == "__main__":
    unittest.main()

