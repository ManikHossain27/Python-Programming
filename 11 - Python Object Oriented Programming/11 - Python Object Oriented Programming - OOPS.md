# 11 - Python Object Oriented Programming - OOPS

## Python Class, Object, Method, Static Method, and Constructor

Python is an object-oriented programming (OOP) language. The main building blocks of OOP
in Python are classes, objects, methods, and constructors.

## Class
- A class is a blueprint or template to create objects.
- It can contain
- Variables (class variables or instance variables)
- Methods (functions inside a class)
Example
```python
class MyClass
def myfun(self)
pass # simple method, does nothing

def display(self, name)
print(name)
```

Here, MyClass is a class with two methods.

## Object
- An object is an instance of a class.
- We create an object by calling the class like a function:
Example
```python
mc1 = MyClass() # object of MyClass

mc1.display("scott") # calling method using object
```

- Each object can access the methods and variables defined inside the class.
- You can also create multiple objects of the same class:
```python
obj1 = MyClass()
obj2 = MyClass()
```

## Instance Method
- A method defined inside a class that takes self as the first parameter.
- self refers to the object that is calling the method.
- Instance methods need an object to be called.
Example
```python
class MyClass
def m1(self): # instance method
print("this is instance method...")

mc = MyClass()

mc.m1() # call using object
```

## Static Method
- Defined inside a class using @staticmethod.
- Does not need self (object reference). Even if you specify self, that will be treated as
parameter.
- Can be called using both class name or object.
Example
```python
class MyClass
@staticmethod

def m2(x, y)
print(x, y)

MyClass.m2(10, 20) # called using class

mc = MyClass()

mc.m2(100, 200) # called using object
```

## Class Variables vs Instance Variables vs Local Variables

- Class Variables: Declared inside a class but outside methods. Shared by all objects.
- Instance Variables: Declared using self. inside methods. Different for each object.
- Local Variables: Declared inside a method (normal function variables).
Example
i, j = 15, 25 # global variables
```python
class MyClass
```

a, b = 10, 20 # class variables

```python
def add(self, x, y)
print(x + y) # local variables
print(self.a + self.b) # class variables
print(i + j) # global variables

mc = MyClass()

mc.add(100, 200)
```

## Constructor (__init__)
- A special method in Python (__init__) that gets called automatically when an object
is created.
- Used to initialize instance variables.
- Similar to a constructor in Java or C++.
Example
```python
class MyClass
def __init__(self): # constructor
print("this is constructor..")

def m1(self)
print("hello...")

mc = MyClass() # constructor is invoked automatically

mc.m1() # normal method must be called explicitly
```

## Constructor with Parameters
Constructors can accept parameters to initialize object data.
Example
```python
class Emp
def __init__(self, eid, ename, sal):

self.eid = eid
self.ename = ename
self.sal = sal

def display(self)
print(self.eid, self.ename, self.sal)

e1 = Emp(101, "john", 500000)

e1.display() # 101 john 500000
```

__str__() Method
- A special method that defines how an object is represented as a string.
- When you use print(object), Python calls __str__() internally.
Example
```python
class Emp
def __init__(self, eid, ename, sal):

self.eid = eid
self.ename = ename
self.sal = sal

def __str__(self)
return self.ename # must return string only

e1 = Emp(101, "john", 500000)

print(e1) # Output: john
```

### Key Takeaways
1. Class = blueprint, Object = real entity created from class.
2. Instance methods use self, need object to call.
3. Static methods use @staticmethod, can be called without object.
4. Class variables are shared across all objects; instance variables are unique per
object.
5. Constructor (__init__) runs automatically when an object is created.
6. __str__() is used to define a string representation of an object.
