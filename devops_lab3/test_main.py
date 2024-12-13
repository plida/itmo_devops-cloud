import main
import unittest

def test_calculate():
    assert main.calculate(100, 60, "-") == 40

if __name__ == '__main__':
    unittest.main()
