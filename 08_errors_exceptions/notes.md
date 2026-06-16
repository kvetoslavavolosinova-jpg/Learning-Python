08_ERRORS_AND_EXCEPTIONS (Python)

1. BASIC CONCEPT
- Errors stop program execution.
- Exceptions are runtime errors that can be handled.
- Goal: prevent crash and control program flow.

------------------------------------------------------------
2. TYPES OF ERRORS

A) SyntaxError
- Happens when Python code is written incorrectly.
- Detected before execution.

Example:
if True
    print("Hello")   # missing colon

------------------------------------------------------------

B) Runtime Errors (Exceptions)
- Occur during execution.

Common ones:

1. NameError
- Variable not defined.
print(x)

2. TypeError
- Wrong type operation.
"5" + 5

3. ValueError
- Correct type, wrong value.
int("abc")

4. ZeroDivisionError
10 / 0

5. IndexError
lst = [1,2,3]
lst[10]

6. KeyError
dict = {"a":1}
dict["b"]

7. AttributeError
"hello".push()

------------------------------------------------------------
3. TRY / EXCEPT (EXCEPTION HANDLING)

Basic structure:

try:
    risky_code()
except:
    handle_error()

Example:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

------------------------------------------------------------
4. MULTIPLE EXCEPT BLOCKS

try:
    x = int(input())
    result = 10 / x
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")

------------------------------------------------------------
5. ELSE BLOCK
- Runs only if no exception occurs.

try:
    x = 5 / 1
except ZeroDivisionError:
    print("Error")
else:
    print("Success")

------------------------------------------------------------
6. FINALLY BLOCK
- Always executes (error or no error).
- Used for cleanup.

try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found")
finally:
    print("This always runs")

------------------------------------------------------------
7. RAISING EXCEPTIONS (raise)

Used to force an error.

Example:
age = -5
if age < 0:
    raise ValueError("Age cannot be negative")

------------------------------------------------------------
8. CUSTOM EXCEPTIONS

class MyError(Exception):
    pass

raise MyError("Something went wrong")

------------------------------------------------------------
9. BEST PRACTICES
- Catch specific exceptions, not generic except:
- Do not hide errors silently
- Use finally for cleanup (files, connections)
- Use raise for invalid business rules
- Keep try blocks small

------------------------------------------------------------
10. FLOW SUMMARY

Code -> Error occurs ->
    try detects ->
        except handles OR
        else runs if OK ->
    finally always runs