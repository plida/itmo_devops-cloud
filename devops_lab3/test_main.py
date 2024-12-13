import main
import unittest

class TestCalc(unitest.TestCase):
    def test_calculate(self):
        self.assertEqual(main.calculate(100, 60, "-"), 40)

if __name__ == '__main__':
    unittest.main()
