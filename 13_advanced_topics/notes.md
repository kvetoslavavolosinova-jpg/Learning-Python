# 13 - Advanced Topics

## 1. List Comprehensions
- A shorter, cleaner, and faster way to create new lists from existing ones.
- Instead of writing a 3-to-4 line `for` loop with `.append()`, we can do it in a single line.
- **Syntax**: `new_list = [expression for item in iterable if condition]`

## 2. Lambda Functions
- Anonymous, one-line functions that we use when we need a simple operation once.
- They do not need the `def` keyword or a `return` statement.
- **Syntax**: `lambda arguments: expression`
- Highly powerful when combined with Pandas `.apply()` method for quick data cleaning.

## 3. Useful Built-in Functions: `zip()` and `enumerate()`
- `enumerate()` -> Returns both the index (0, 1, 2...) and the value while looping.
- `zip()` -> Pairs up elements from two separate lists side-by-side (e.g., pairing supplier names with their ratings).
