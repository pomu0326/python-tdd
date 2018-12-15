import unittest
from money import Money, Bank, Expression

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Money.doller(5)
        self.assertEqual(Money.doller(10), five.times(2))
        self.assertEqual(Money.doller(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.doller(5).equals(Money.doller(5)))
        self.assertFalse(Money.doller(5).equals(Money.doller(6)))
        self.assertFalse(Money.franc(5).equals(Money.doller(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.doller(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_simple_addition(self):
        five = Money.doller(5)
        sum:Expression = five.plus(five)
        self.assertEqual(Money.doller(10), sum)
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertEqual(Money.doller(10), reduced)

if __name__ == "__main__":
    unittest.main()

