import pytest
from calculator import QuickCalc

@pytest.fixture
def calc():
    return QuickCalc()

# --- UNIT TESTS (Minimum 8) ---

def test_addition(calc):
    assert calc.add(5, 3) == 8

def test_subtraction(calc):
    assert calc.subtract(10, 4) == 6

def test_multiplication(calc):
    assert calc.multiply(6, 7) == 42

def test_division(calc):
    assert calc.divide(10, 2) == 5

def test_division_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

def test_addition_with_negatives(calc):
    assert calc.add(-5, -3) == -8

def test_multiplication_with_floats(calc):
    assert calc.multiply(2.5, 4.0) == 10.0

def test_large_numbers_subtraction(calc):
    assert calc.subtract(1000000, 999999) == 1

# --- INTEGRATION TESTS (Minimum 2) ---

def test_integration_full_calculation_flow(calc):
    # Simulate: User enters 5, adds 3
    result1 = calc.add(5, 3)
    calc.current_value = result1
    
    # User multiplies the result by 2
    final_result = calc.multiply(calc.current_value, 2)
    assert final_result == 16

def test_integration_clear_after_calculation(calc):
    # Simulate: User does a calculation
    calc.current_value = calc.add(50, 50)
    assert calc.current_value == 100
    
    # User presses Clear
    cleared_val = calc.clear()
    assert cleared_val == 0.0
    assert calc.current_value == 0.0