# 2 - Datatypes, Operators & Concatenation - Python basics

## Python Basics

- Deleting Variables
- Data Types
- Operators
- Concatenation
- User Input
- Type Conversion/Type Casting

## Deleting Variables
- Use del to remove a variable from memory.
- Once deleted, you can’t use it until recreated.
```python
a = 100
b = 200

del a
print(b) # Works → 200
```

## Basic Data Types
- int → whole numbers (10, -5)
- float → decimal numbers (3.14, -0.5)
- str → text/strings ("Hello", 'Python')
- bool → True or False

```python
x = 100 # int
y = 10.5 # float
s = "Python" # str
b = True # bool

print(type(x)) # <class 'int'>
```

## Operators
- Arithmetic: +, -, *, /, %, ** (power), // (floor division)
- Comparison: ==, !=, >, <, >=, <= → returns True/False
- Logical: and, or, not → returns True/False

## Concatenation
- + joins same-type values.
- Works for numbers, strings, and booleans (True=1, False=0).

```python
print('Hello' + 'Python') # HelloPython
print(True + 5) # 6
```

## Taking User Input
- input() → always returns string → convert if needed.
```python
name = input("Enter name: ")
num1 = int(input("Enter number: "))
num2 = float(input("Enter decimal: "))
```

## Type Casting
- Change data type: int(), float(), str().
```python
x = "10"
y = int(x) # "10" → 10
```
