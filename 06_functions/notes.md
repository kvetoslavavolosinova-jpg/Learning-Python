06 — FUNCTIONS in Python

What is a function
A function is a reusable block of code that performs a specific task.

Functions are used for:
- code reuse
- better structure and readability
- breaking problems into smaller parts

Basic syntax
def function_name():
    print("Hello")

Calling a function
function_name()

Functions with parameters
def greet(name):
    print("Hello", name)

greet("Anna")

- parameter = variable in function definition
- argument = actual value passed

Multiple parameters
def add(a, b):
    print(a + b)

add(3, 5)

Return statement
def add(a, b):
    return a + b

result = add(3, 5)
print(result)

print vs return
print() → only displays output
return → gives value back for later use

Why return is important
- store results in variables
- use in further calculations
- combine functions

Default parameters
def greet(name="user"):
    print("Hello", name)

greet()
greet("Eva")

Types of functions

No parameters
def hello():
    print("Hello")

With parameters
def greet(name):
    print(name)

With return
def double(x):
    return x * 2

Variable scope

Local variable (inside function)
def test():
    x = 10
    print(x)

Global variable (outside function)
x = 10

def test():
    print(x)

Scope rule
Variables created inside a function cannot be used outside it.

def test():
    x = 5

print(x)  # error

Functions calling functions
def a():
    return 5

def b():
    return a() + 2

Returning multiple values
def calculate(a, b):
    return a + b, a * b

sum_result, product_result = calculate(3, 4)

Boolean functions
def is_even(number):
    return number % 2 == 0

Common mistakes

Missing parentheses
def test:

Missing return
def add(a, b):
    a + b

Wrong indentation
def test():
print("error")

Core concepts
- what a function is
- how to define (def)
- how to call a function
- parameters vs arguments
- print vs return
- default parameters
- scope (local vs global)
- multiple return values
- boolean functions

Mental model
INPUT → FUNCTION → OUTPUT