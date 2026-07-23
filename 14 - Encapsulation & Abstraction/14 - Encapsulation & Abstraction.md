# 14 - Encapsulation & Abstraction

## Encapsulation in Python

## What is Encapsulation->
- Encapsulation means wrapping variables (data) and methods (functions) into a
single unit (class).
- It also means restricting direct access to some variables so that they cannot be
modified accidentally.
- In Python, we achieve this using access modifiers.

## Why do we need Encapsulation->
1. Data protection – Prevents accidental modification of important data.
2. Controlled access – We decide how the data should be read or modified (using
getters and setters).
3. Security – Hides the implementation details from the outside world.

## Access Modifiers in Python
1. Public (default) → can be accessed anywhere.
self.name # public
2. Protected (convention, single underscore) → should not be accessed directly outside
the class.
self._marks # protected
3. Private (double underscore) → cannot be accessed directly outside the class.
self.__balance # private

### Example of Encapsulation
```python
class Student
def __init__(self, name)

self.name = name
self.__marks = 0 # private variable
```

```python
# Getter method
```

```python
def get_marks(self)
return self.__marks
```

```python
# Setter method
```

```python
def set_marks(self, marks)
if 0 <= marks <= 100:

self.__marks = marks

else
print("Invalid marks! Must be between 0 and 100.")
```

```python
# Usage
```

```python
s1 = Student("Rahul")

s1.set_marks(90) # setting value through setter

print(s1.get_marks()) # getting value through getter
```

## Abstraction in Python

Data abstraction means showing only the essential features and hiding the complex internal
details.
In Python abstraction is used to hide the implementation details from the user and expose
only necessary parts.

## Abstract Base Class (ABC)

- In Python, an Abstract Base Class (ABC) is used to achieve data abstraction by
defining a common interface for its subclasses.
-
It cannot be instantiated directly and serves as a blueprint for other classes.

### Example

```python
from abc import ABC, abstractmethod

class Greet(ABC)
@abstractmethod

def say_hello(self)
pass # Abstract method

class English(Greet)
def say_hello(self)
return "Hello!"

g = English()

print(g.say_hello())
```

## Explanation
- Greet is an abstract class with a method say_hello() that has no implementation.
- English implements this method and returns a greeting.
- This keeps structure fixed while letting subclasses define their own behavior.

## Abstract Class Instantiation
- Abstract classes cannot be instantiated directly. This is because they contain one or
more abstract methods or properties that lack implementations.

- Attempting to instantiate an abstract class results in a TypeError.
