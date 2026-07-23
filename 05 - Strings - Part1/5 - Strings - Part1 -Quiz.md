# 5 - Strings - Part1 -Quiz

## Python Strings – Quiz

Q1. Which of the following is the correct way to create a string in Python->
a) name = "john"
b) name = 'john'
c) name = str("john")
d) All of the above

Q2. What is the type of the following variable->
```python
x = "hello"

print(type(x))
```

a) <class 'int'>
b) <class 'str'>
c) <class 'list'>
d) <class 'object'>

Q3. What will be the output of this code->
```python
name = str()

print(name)
```

a) "str"
b) None
c) "" (empty string)
d) Error

## Q4. Strings in Python are
a) Mutable
b) Immutable
c) Both
d) None

Q5. Which of the following is NOT an immutable data type in Python->
a) Numbers
b) Tuples
c) Lists
d) Strings

Q6. What happens when you concatenate two strings using +->
a) Adds them like numbers
b) Joins them together
c) Multiplies them
d) Throws an error

## Q7. What is the result of
```python
print("hi" * 3)
```

a) hihihi
b) hi3
c) error
d) [hi, hi, hi]

```python
Q8. What will mystr = "welcome"; print(mystr[1:3]) output->
```

a) we
b) el
c) lc
d) co

```python
Q9. What will mystr = "welcome"; print(mystr[:6]) output->
```

a) welcom
b) welcome
c) welc
d) Error

## Q10. Negative indexes in Python strings count from
a) Left to right
b) Right to left
c) Randomly
d) None

## Q11. What is the output of
```python
s = "welcome"
print(s[1:-1])
```

a) elcom
b) welcome
c) elco
d) w

## Q12. What is the result of
```python
s = "welcome"
print(s[-5:-2])
```

a) lco
b) wel
c) com
d) w

Q13. Which is the preferred way to format strings in Python 3.6+->
a) format()
b) % operator
c) f-strings
d) concatenation

## Q14. What is the output of
```python
age = 25
print(f"I am {age} years old")
```

a) I am age years old
b) I am 25 years old
c) I am {age} years old
d) Error

## Q15. What is the output of
```python
price = 50
print(f"Price: {price:.2f}")
```

a) Price: 50
b) Price: 50.00
c) Price: 50.000
d) Error

Q16. Which of these methods can replace f-strings in older Python versions->
a) .upper()
b) .format()
c) .replace()
d) .join()

## Q17. What is the output of
```python
s = "welcome"

print("come" in s)
```

a) True
b) False
c) Error
d) None

## Q18. What is the result of
"python" not in "welcome to python"
a) True
b) False
c) Error
d) None

## Q19. What is the output of "hello".capitalize()->
a) Hello
b) hello
c) HELLO
d) Error

## Q20. Which method converts ALL characters to lowercase->
a) lower()
b) upper()

c) capitalize()
d) title()

Q21. Which method is more aggressive than lower() in handling Unicode characters->
a) casefold()
b) lowercase()
c) smallcase()
d) title()

## Q22. What does "WELCOME".swapcase() return->
a) WELCOME
b) welcome
c) wELCOME
d) error

## Q23. "hello world".title() returns
a) Hello world
b) Hello World
c) HELLO WORLD
d) Error

## Q24. What is the result of
```python
s = "Hi"
print(s.center(6, '*'))
```

a) **Hi**
b) Hi****
c) ****Hi
d) Error

## Q25. What is the output of
```python
print("My name is {}".format("John"))
```

a) My name is {}
b) My name is John
c) Error
d) None

## Q26. What does "hello".find("l") return->
a) 1
b) 2
c) 3
d) -1

Q27. What happens if substring not found using .index()->
a) Returns -1
b) Raises ValueError
c) Returns None
d) Crashes Python

## Q28. "banana".count("a") returns
a) 2
b) 3
c) 4
d) Error

## Q29. "Hello World".replace("World", "Python") returns
a) Hello World
b) Hello Python
c) Error
d) None

## Q30. "abc123".isalnum() returns
a) True
b) False
c) Error
d) None

## Q31. Which will return False->
a) "Hello".isalpha()
b) "123".isdecimal()
c) "12.5".isdigit()
d) "123".isnumeric()

## Q32. "HELLO".islower() returns
a) True
b) False
c) Error
d) None

## Q33. "python".isupper() returns
a) True
b) False
c) Error
d) None

## Q34. "one,two,three".split(",") returns
a) ['one,two,three']
b) ['one', 'two', 'three']
c) ('one', 'two', 'three')
d) Error

## Q35. "hello".startswith("he") returns
a) True
b) False
c) Error
d) None

## Q36. "hello.py".endswith(".py") returns
a) True
b) False
c) Error
d) None

## Q37. " hi ".strip() returns
a) "hi"
b) " hi "
c) " hi"
d) "hi "

## Q38. " hi".lstrip() returns
a) "hi"
b) " hi"
c) "hi "
d) "hi "

## Q39. "hi ".rstrip() returns
a) "hi"
b) "hi "
c) " hi"
d) "h"

## Q40. What will this code output->
```python
s = "Python"
print(s[0] + s[-1])
```

a) Pn
b) Po
c) Ph
d) Py

## Q41. Predict the output
```python
s = "Hello"

print(s * 2)
```

a) HelloHello
b) Hello2
c) HHeelllloo
d) Error

## Q42. What will this print->
```python
s = "python"

print(s.upper().lower().capitalize())
```

a) python
b) Python
c) PYTHON
d) Error

## Q43. Find the output
```python
s = "data"
print(s.replace("a", "o"))
```

a) dato
b) doto
c) dodo
d) dotoa

## Q44. Output of
```python
print("hello".find("x"))
```

a) 0
b) -1
c) None
d) Error

## Q45. What will this output->
```python
txt = "Python"

print(txt.startswith("P") and txt.endswith("n"))
```

a) True
b) False
c) None
d) Error

## Q46. What will be printed->
```python
s = "abc123"

print(s.isalpha())
```

a) True
b) False
c) Error
d) None

Q47. Which will output ['10', '20', '30']->
a) "10,20,30".split(",")
b) "10 20 30".split(",")
c) "10|20|30".split(",")
d) "10 20 30".split()

## Q48. What is the result->
```python
print("pyTHon".swapcase())
```

a) python
b) PYTHON
c) PYthON
d) PyThOn

## Q49. What will be printed->
```python
s = "python"

print(len(s))
```

a) 5
b) 6
c) 7
d) Error

## Q50. Which code will print "Hello World"->
a) print("Hello" + "World")
b) print("Hello" " " "World")
c) print("Hello" * "World")
d) print("Hello", "World")

## Answers
1-d, 2-b, 3-c, 4-b, 5-c, 6-b, 7-a,
8-b, 9-a, 10-b, 11-a, 12-a,
13-c, 14-b, 15-b, 16-b,
17-a, 18-b,
19-a, 20-a, 21-a, 22-b, 23-b,
24-a, 25-b,
26-b, 27-b,
28-b, 29-b,
30-a, 31-c, 32-b, 33-b,
34-b, 35-a, 36-a, 37-a, 38-a, 39-a,
40-c, 41-a, 42-b, 43-b, 44-b,
45-a, 46-b, 47-a, 48-c, 49-b, 50-b/d
