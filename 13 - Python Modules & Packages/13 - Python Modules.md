# 13 - Python Modules

## Python Modules

## What is a Module->
- A module in Python is simply a Python file (.py) that contains functions, classes, or
variables.
- Modules help in organizing code and reusing it across multiple programs.
- Example: If you have math.py with functions, you can use them in another file with
```python
import math.
```

### Example 1: Using Functions from a Module
Files
operations.py
```python
def add(num1, num2)
print(num1 + num2)
def mul(num1, num2)
print(num1 * num2)
```

client.py
```python
# Approach 1: Import whole module
```

```python
import operations

operations.add(10, 20)
operations.mul(10, 20)
```

```python
# Approach 2: Import specific functions
```

```python
from operations import add, mul

add(10, 20)
mul(10, 20)
```

```python
# Approach 3: Import everything
```

```python
from operations import *
add(10, 20)
mul(10, 20)
```

## Key Points
- import module_name → use with module_name.function().
- from module_name import func1, func2 → directly call the functions.
- from module_name import * → imports all functions, but may cause conflicts if two
modules have functions with the same name.

### Example 2: Same Function Names in Two Modules
Files
animal.py
```python
def fly()
print("Animal Cant fly")
def color()
print("Animal is Black")
```

bird.py
```python
def fly()
print("Bird Can Fly")
def color()
print("Bird is Green")
```

main.py
```python
# Approach 1: Import modules separately
```

```python
import animal
import bird

animal.fly()
animal.color()

bird.fly()
bird.color()
```

```python
# Approach 2: Import everything from both
```

```python
from animal import *

fly()
color()

from bird import *

fly()
color()
```

## Key Points
- If two modules have functions with the same name, importing with from module
```python
import * may cause confusion.
```

- To avoid conflicts, prefer approach 1 (use module_name.function()).

### Example 3: Classes in Different Modules
Files
a.py
```python
class Animal
def display(self)
print("I like Cow")
```

b.py
```python
class Bird
def display(self)
print("I like Parrot")
```

main.py
```python
# Approach 1: Import modules
```

```python
import a
import b
obj1 = a.Animal()

obj1.display()

obj2 = b.Bird()

obj2.display()
```

```python
# Approach 2: Import classes directly
```

```python
from a import Animal
from b import Bird

obj3 = Animal()

obj3.display()

obj4 = Bird()

obj4.display()
```

## Key Points
- You can import entire modules or specific classes.
- If only one or two classes are needed, direct import is cleaner.
- If many functions/classes are needed, import the full module.
