import unittest
from doller import Doller

class TestMoney(unittest.TestCase):
    def test_multiplication(self):
        five = Doller(5)
        five.times(2)
        self.assertEquals(10, five.amount)

if __name__ == "__main__":
    unittest.main()

