import unittest
from money import Money, Bank, Expression, Sum

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
        bank = Bank()
        reduced = bank.reduce(sum, 'USD')
        self.assertEqual(Money.doller(10), reduced)

    def test_plus_return_sum(self):
        five = Money.doller(5)
        sum = five.plus(five)
        self.assertIsInstance(sum, Sum)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)

    def test_reduce_sum(self):
        sum = Sum(Money.doller(3), Money.doller(4))
        self.assertIsInstance(sum, Expression)
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.doller(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.doller(1), "USD")
        self.assertEqual(Money.doller(1), result)

if __name__ == "__main__":
    unittest.main()

