# Python Collections

## What are Collections?

Collections are data structures used to store multiple values in a single variable.

Python provides four built-in collection types:

* **List**
* **Tuple**
* **Set**
* **Dictionary**

Each collection type has different properties and use cases.

---

# 1. List (`list`)

A **list** is an ordered and mutable collection.

### Properties

* Ordered
* Mutable (can be changed)
* Allows duplicate values

### Example

```python
fruits = ["apple", "banana", "cherry"]
```

### Access Elements

```python
print(fruits[0])
```

Output:

```
apple
```

### Common Methods

```python
fruits.append("orange")
fruits.remove("banana")
fruits.pop()
```

---

# List Slicing

You can access part of a list using slicing.

```python
numbers = [1, 2, 3, 4, 5]

numbers[1:4]
numbers[:3]
numbers[-1]
```

Output:

```
[2, 3, 4]
[1, 2, 3]
5
```

---

# Loop Through a List

```python
for fruit in fruits:
    print(fruit)
```

---

# 2. Tuple (`tuple`)

A **tuple** is an ordered and immutable collection.

### Properties

* Ordered
* Immutable (cannot be changed)
* Allows duplicate values

### Example

```python
coordinates = (10, 20)
```

Access an element:

```python
print(coordinates[0])
```

---

# 3. Set (`set`)

A **set** is an unordered collection of unique values.

### Properties

* Unordered
* Mutable
* Does not allow duplicates

### Example

```python
numbers = {1, 2, 3, 3, 2}
print(numbers)
```

Output:

```
{1, 2, 3}
```

Sets are useful for removing duplicate values.

---

# 4. Dictionary (`dict`)

A **dictionary** stores data as key-value pairs.

### Properties

* Ordered (Python 3.7+)
* Mutable
* Keys must be unique

### Example

```python
person = {
    "name": "Anna",
    "age": 25,
    "city": "Zurich"
}
```

Access a value:

```python
print(person["name"])
```

Modify a value:

```python
person["age"] = 26
```

---

# Useful Dictionary Methods

```python
person.keys()
person.values()
person.items()
```

Loop through a dictionary:

```python
for key, value in person.items():
    print(key, value)
```

---

# Nested Collections

Collections can contain other collections.

Example:

```python
students = [
    {"name": "Anna", "age": 20},
    {"name": "Peter", "age": 22}
]
```

Nested collections are commonly used when working with JSON files, APIs, and data analysis.

---

# List Comprehension

List comprehension provides a concise way to create lists.

```python
numbers = [1, 2, 3, 4]

squares = [x * x for x in numbers]
```

Output:

```
[1, 4, 9, 16]
```

---

# Summary

| Collection | Ordered | Mutable | Duplicates          |
| ---------- | ------- | ------- | ------------------- |
| List       | Yes     | Yes     | Yes                 |
| Tuple      | Yes     | No      | Yes                 |
| Set        | No      | Yes     | No                  |
| Dictionary | Yes     | Yes     | Keys must be unique |

---

# Key Takeaways

* **Lists** are the most commonly used collection type.
* **Tuples** are useful for fixed data.
* **Sets** store unique values and remove duplicates.
* **Dictionaries** store data as key-value pairs.
* **Nested collections** are widely used in real-world datasets.
* **List comprehensions** provide a clean and efficient way to create new lists.

