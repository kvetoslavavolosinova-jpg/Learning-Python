# 11 - Testing & Debugging

## 1. Automated Testing (Automatizované testovanie)
- **Manual Testing**: Running the code and manually checking the terminal. Slow and prone to human error.
- **Automated Testing**: Writing special code (tests) whose only job is to run our main code with various inputs and verify the outputs.
- **Regression**: When we change or optimize our code in the future, automated tests make sure we did not accidentally break existing functionality.

## 2. Unit Testing in Python (`unittest`)
- **Unit Test**: Tests a single, small "unit" of code (usually a single function) in isolation.
- Python has a built-in library called `unittest`.
- We create a test class that inherits from `unittest.TestCase`.
- Inside the class, every test method **must start with the word `test_`** (otherwise Python will ignore it).

### Common Assertions (Tvrdenia):
- `self.assertEqual(actual, expected)` -> Checks if the two values are equal.
- `self.assertTrue(x)` -> Checks if `x` is True.
- `self.assertFalse(x)` -> Checks if `x` is False.

## 3. Debugging & Reading Tracebacks
- **Debugging**: The process of identifying, analyzing, and fixing bugs (errors) in the code.
- **Print Debugging**: Placing `print(variable)` inside functions to check their values during execution.
- **Reading Tracebacks**: When Python crashes, read the error message **from the bottom up**:
  1. The very last line tells you the **Error Type and Message** (e.g., `ZeroDivisionError`).
  2. A few lines above tells you the **exact file and line number** where the crash happened.
