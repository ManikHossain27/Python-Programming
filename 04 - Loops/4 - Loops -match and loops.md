# 4 - Loops -match and loops

## Match, Range () function & Loops in Python

## Python match Statement
- Used to choose one block of code to run from multiple options (like switch in other
languages).
- Why use it-> It’s cleaner than writing many if...elif...else statements.
- Syntax
match expression
case value1
```python
# code block
```

case value2
```python
# code block
```

case _
```python
# default block (if no match)
```

- How it works
1. The expression is checked once.
2. Compared with each case value.
3. If a match is found, that block runs.

range() Function
- Generates a sequence of numbers.
- Syntax: range(start, stop, step)
- Notes
- start → beginning number (default 0)
- stop → end number (exclusive)
- step → how much to increase/decrease each time (default 1)

## Looping Statements
1. While Loop – Runs while the condition is True.
```python
while condition

# repeat code
```

2. For Loop – Runs a fixed number of times, often with range().
```python
for variable in range(start, stop, step):
```

```python
# repeat code
```

## Jumping Statements
- break → stop the loop immediately.
- continue → skip the current iteration, go to the next one.
