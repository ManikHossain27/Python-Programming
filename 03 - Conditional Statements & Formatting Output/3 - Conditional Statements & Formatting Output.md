# 3 - Conditional Statements & Formatting Output

## Python Conditional Statements

- Conditional statements are used to make decisions in Python.
- They allow the program to execute different blocks of code depending on a condition
(True or False).

## Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the
code. Other programming languages often use curly-brackets for this purpose.
1. if Statement
The if statement executes a block of code only if the condition is True.
Syntax
```python
if condition

# code to execute if condition is True
```

Example
```python
age = 18
if age >= 18:
print("You are eligible to vote.")
```

### Output
You are eligible to vote.

### 2. if...else Statement
The else block runs when the if condition is False.
Syntax
```python
if condition

# code if condition is True
```

```python
else
```

```python
# code if condition is False
```

### Example
```python
age = 16
if age >= 18:

print("You are eligible to vote.")

else
print("You are not eligible to vote.")
```

### Output
You are not eligible to vote.

### 3. if...elif...else Statement
Used when you have multiple conditions to check.
Syntax
```python
if condition1

# code if condition1 is True
```

```python
elif condition2
```

```python
# code if condition2 is True
```

```python
else
```

```python
# code if none of the conditions are True
```

Example
```python
marks = 75
if marks >= 90:

print("Grade: A")
elif marks >= 75:

print("Grade: B")
elif marks >= 50:

print("Grade: C")

else
print("Fail")
```

### Output
Grade: B

## Short Hand If
If you have only one statement to execute, you can put it on the same line as the if

statement.
Example
One line if statement
```python
if a > b: print("a is greater than b")
```

## Short Hand If ... Else (Ternary Operator)
If you have only one statement to execute, one for if, and one for else, you can put it all on

the same line
Example
One line if else statement
```python
a = 2
b = 330

print("A") if a > b else print("B")
```

You can also have multiple else statements on the same line:
Example
One line if else statement, with 3 conditions:
```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```

## And
The and keyword is a logical operator, and is used to combine conditional statements:
Example
Test if a is greater than b, AND if c is greater than a:

```python
a = 200
b = 33
c = 500
if a > b and c > a:

print("Both conditions are True")
```

## Or
The or keyword is a logical operator, and is used to combine conditional statements:
Example
Test if a is greater than b, OR if a is greater than c:
```python
a = 200
b = 33
c = 500
if a > b or a > c:
print("At least one of the conditions is True")
```

## Not
The not keyword is a logical operator, and is used to reverse the result of the conditional
statement
Example
Test if a is NOT greater than b:
```python
a = 33
b = 200

if not a > b
print("a is NOT greater than b")
```

## Nested If
You can have if statements inside if statements, this is called nested if statements.
Example
```python
x = 41

if x > 10
print("Above ten,")

if x > 20
print("and also above 20!")

else
print("but not above 20.")
```

## The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no

content, put in the pass statement to avoid getting an error.
Example
```python
a = 33
b = 200

if b > a
pass
```
