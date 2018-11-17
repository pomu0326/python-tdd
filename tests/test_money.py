import unittest
from money import Money, Doller, Franc

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_franc_multiplication(self):
        five = Money.franc(5)
        self.assertEqual(Money.franc(10), five.times(2))
        self.assertEqual(Money.franc(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.doller(5).equals(Money.doller(5)))
        self.assertFalse(Money.doller(5).equals(Money.doller(6)))
        self.assertTrue(Money.franc(5).equals(Money.franc(5)))
        self.assertFalse(Money.franc(5).equals(Money.franc(6)))
        self.assertFalse(Money.franc(5).equals(Money.doller(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.doller(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

if __name__ == "__main__":
    unittest.main()

