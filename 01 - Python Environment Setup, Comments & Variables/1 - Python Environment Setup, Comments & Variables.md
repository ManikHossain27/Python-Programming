# 1 - Python Environment Setup, Comments & Variables

## Python Basics

- Introduction to Python
- Setup Environment
- Comments
- Keywords
- Variables
Python Programming
- Python is a high-level, general-purpose programming language.
- It is open-source (free to use and modify).
- It is platform-independent – runs on Windows, macOS, Linux, etc.
Why Python?
- Simple and easy to learn.
- Large community support.
- Works for web development, data science, automation, AI, and more.
Download and Install Python
- Go to python.org → Download → Install on your system.
PyCharm
- PyCharm is a popular IDE (Integrated Development Environment) for Python.
- Helps in writing, running, and debugging Python code easily.
Comments in Python
- Comments are non-executable text in code.
- Python ignores comments while running.
Uses
- Explain code.
- Make code easier to read.
- Temporarily disable code during testing.
- Single-line comment: starts with #
```python
# This is a comment
```

- Multi-line comment: use triple quotes (''' or """)
```python
"""

This is a
multi-line comment
"""
```

## Keywords
- Reserved words in Python that have special meaning.
- Examples: if, else, while, for, True, False, None, etc.
- You cannot use keywords as variable names.

## Variables
- Containers for storing data values.
- No need to declare before using.
- Python decides the data type automatically.
- Variable names are case-sensitive (name and Name are different).
Example
```python
x = 10 # integer
name = "John" # string
```

## Variable Naming Conventions
- Can be short (x, y) or descriptive (age, car_name).
Rules
- Must start with a letter or underscore.
- Cannot start with a number.
- Only letters, numbers, and underscores are allowed.
- Case-sensitive.
- Cannot be a Python keyword.

### Valid Examples
```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Invalid Examples
```python
2myvar = "John" # starts with number

my-var = "John" # contains hyphen
my var = "John" # contains space
```

## Dynamic Typing
- Python is a dynamically typed language.
- You don’t need to declare a variable type—it is decided at runtime.
Example
```python
x = 10 # int
x = "Hello" # now a string
```
