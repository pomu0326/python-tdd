import unittest
from doller import Doller
from franc import Franc

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Doller(5)
        self.assertEqual(Doller(10), five.times(2))
        self.assertEqual(Doller(15), five.times(3))

    def test_franc_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Doller(5).equals(Doller(5)))
        self.assertFalse(Doller(5).equals(Doller(6)))

if __name__ == "__main__":
    unittest.main()

