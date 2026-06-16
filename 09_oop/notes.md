# 09 – Object-Oriented Programming (OOP)

## 1. What is OOP?

OOP (Object-Oriented Programming) is a programming style based on objects.

Think about real life:

- Dog 🐶
- Car 🚗
- Person 👩
- Phone 📱

Every object has:

- attributes (name, color, age...)
- actions (run, drive, call...)

In Python, we create these objects using OOP.

---

## 2. Class

A **class** is a blueprint or template.

It is like a recipe or a house plan.

From one class, we can create many objects.

```python
class Dog:
    pass
```

This creates an empty class called `Dog`.

---

## 3. Object (Instance)

An **object** is a real copy of a class.

Example:

- Class = recipe
- Object = baked cake

```python
class Dog:
    pass

dog1 = Dog()
dog2 = Dog()
```

Now we have two different objects.

---

## 4. __init__() Constructor

`__init__()` is a special method.

It runs automatically when a new object is created.

```python
class Dog:

    def __init__(self):
        print("New dog")
```

```python
dog = Dog()
```

Output:

New dog

---

## 5. self

`self` means:

**"this object"**

If there are two dogs:

- Rex
- Max

`self` always refers to the object currently being used.

---

## 6. Attributes

Attributes are the data stored inside an object.

```python
class Dog:

    def __init__(self):
        self.name = "Rex"
```

```python
dog = Dog()

print(dog.name)
```

Output:

Rex

`name` is an attribute.

---

## 7. Parameters in __init__()

Values can be passed when creating an object.

```python
class Dog:

    def __init__(self, name):
        self.name = name
```

```python
dog = Dog("Rex")

print(dog.name)
```

Output:

Rex

Another object:

```python
dog2 = Dog("Max")
```

Each object has its own data.

---

## 8. Multiple Attributes

An object can have multiple attributes.

```python
class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

```python
dog = Dog("Rex", 5)
```

The object now has:

- name
- age

---

## 9. Methods

A method is a function that belongs to an object.

```python
class Dog:

    def bark(self):
        print("Woof!")
```

```python
dog = Dog()

dog.bark()
```

Output:

Woof!

---

## 10. Methods Can Use Attributes

```python
class Dog:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am", self.name)
```

```python
dog = Dog("Rex")

dog.introduce()
```

Output:

I am Rex

---

## 11. Changing Attributes

Object attributes can be changed.

```python
class Dog:

    def __init__(self, name):
        self.name = name
```

```python
dog = Dog("Rex")

dog.name = "Max"

print(dog.name)
```

Output:

Max

---

## 12. Example – Person Class

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("Hello!")
```

```python
person = Person("Anna", 25)

person.hello()
```

---

## 13. Example – Car Class

```python
class Car:

    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print("Car is driving")
```

```python
car = Car("BMW")

car.drive()
```

---

## 14. __str__()

`__str__()` defines what will be printed when using:

```python
print(object)
```

Example:

```python
class Dog:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
```

```python
dog = Dog("Rex")

print(dog)
```

Output:

Rex

---

## 15. Inheritance

One class can inherit from another class.

Example:

- Animal
- Dog

Every dog is an animal.

```python
class Animal:

    def speak(self):
        print("Sound")
```

```python
class Dog(Animal):
    pass
```

```python
dog = Dog()

dog.speak()
```

Output:

Sound

---

## 16. Method Overriding

A child class can replace a parent's method.

```python
class Animal:

    def speak(self):
        print("Sound")
```

```python
class Dog(Animal):

    def speak(self):
        print("Woof!")
```

```python
dog = Dog()

dog.speak()
```

Output:

Woof!

---

## 17. super()

`super()` is used to call the parent class.

```python
class Animal:

    def __init__(self, name):
        self.name = name
```

```python
class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)
```

`super()` runs the parent's code.

---

## 18. isinstance()

Checks whether an object belongs to a class.

```python
dog = Dog("Rex")

print(isinstance(dog, Dog))
```

Output:

True

---

## 19. type()

Shows the type of an object.

```python
print(type(dog))
```

Output:

<class '__main__.Dog'>

---

# Quick Summary

| Term | Meaning |
|----------------|-------------------------|
| Class | Blueprint or template |
| Object | Instance of a class |
| Attribute | Data stored in an object |
| Method | Function of an object |
| self | This object |
| __init__() | Runs when an object is created |
| __str__() | Defines object printing |
| Inheritance | One class inherits another |
| super() | Calls the parent class |
| isinstance() | Checks object type |
| type() | Returns object type |