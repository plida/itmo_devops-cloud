import main

def test_calculate():
    assert main.calculate(5, 2, "*") == 10
    assert main.calculate(90, 3, "/") == 30
    assert main.calculate(1, 0, "+") == 1
    assert main.calculate(100, 60, "-") == 40
