# Quick-Calc

Quick-Calc is a lightweight calculator application written in Python. It supports basic arithmetic operations including addition, subtraction, multiplication, and division, while handling edge cases like division by zero. It also includes a state-clearing function.

## Setup Instructions
1. Ensure you have Python 3 installed.
2. Clone this repository to your local machine.
3. Install the required testing framework by running: pip install pytest

## How to Run Tests
To execute the complete test suite (unit and integration tests), navigate to the root directory of the project and run the following command:
pytest

## Testing Framework Research: Pytest vs Unittest
I chose Pytest for this assignment because its minimal design aligns well with the simplicity of the Quick-Calc application. The ability to use plain assert statements makes the unit tests highly readable, and its built-in pytest.raises context manager handles our division-by-zero edge case cleanly.