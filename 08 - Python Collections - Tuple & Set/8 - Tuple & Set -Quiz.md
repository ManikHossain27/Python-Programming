# 8 - Tuple & Set -Quiz

## Quiz on Python Lists, Sets, and Tuples

## Section A: Python Lists (20 Questions)
Q1. Which symbol is used to create a list in Python->
a) {}
b) []
c) ()
d) <>
Q2. What is the output of
```python
nums = [1, 2, 3, 4]
print(nums[2])
```

a) 1
b) 2
c) 3
d) 4
Q3. Lists in Python are:
a) Immutable
b) Mutable
c) Fixed-length
d) None of the above
Q4. Which method is used to add an element at the end of a list->
a) insert()
b) add()
c) append()
d) extend()
Q5. What does the following code print->
```python
x = [10, 20, 30]

x.append([40, 50])
print(x)
```

a) [10, 20, 30, 40, 50]
b) [10, 20, 30, [40, 50]]
c) Error
d) None

Q6. Which method is used to remove a specific value from a list->
a) remove()
b) pop()
c) delete()
d) discard()
Q7. What will this output->
```python
fruits = ["apple", "banana", "cherry"]

print(len(fruits))
```

a) 2
b) 3
c) 4
d) Error
Q8. What is the result of
```python
list1 = [1, 2, 3]
list2 = [4, 5]

print(list1 + list2)
```

a) [1, 2, 3, 4, 5]
b) [5, 4, 3, 2, 1]
c) Error
d) [1, 2, 3, [4, 5]]
Q9. Which of the following creates an empty list->
a) list()
b) []
c) Both a and b
d) None
Q10. What does list1 * 2 do->
a) Doubles each element
b) Repeats the list elements
c) Multiplies only numeric values
d) Error
Q11. What will this return->
```python
x = [1, 2, 3, 4, 5]
print(x[1:4])
```

a) [1, 2, 3]
b) [2, 3, 4]

c) [3, 4, 5]
d) [2, 3]
Q12. Which method is used to insert an element at a specific position->
a) add()
b) insert()
c) append()
d) extend()
Q13. Which method is used to reverse a list->
a) sort(reverse=True)
b) reverse()
c) flip()
d) None
Q14. What does this print->
```python
x = [1, 2, 3, 4]

print(x.pop())
```

a) 1
b) 4
c) Error
d) None
Q15. Which of the following is correct syntax for list comprehension->
a) [x for x in range(5)]
b) [x; x in range(5)]
c) [x : x in range(5)]
d) [for x in range(5)]
Q16. What is the result->
```python
x = [3, 1, 4, 2]

x.sort()
print(x)
```

a) [3, 1, 4, 2]
b) [1, 2, 3, 4]
c) [4, 3, 2, 1]
d) Error
Q17. Which method is used to extend a list with multiple elements->
a) add()
b) append()
c) extend()
d) insert()

## Q18. What will this print->
```python
x = [10, 20, 30]
y = x

y.append(40)
print(x)
```

a) [10, 20, 30]
b) [10, 20, 30, 40]
c) Error
d) None
Q19. What happens if you try x[100] on a list with 10 elements->
a) Returns last element
b) Error: Index out of range
c) Returns None
d) Empty list
Q20. What will this print->
```python
nums = [1, 2, 3] * 2

print(nums)
```

a) [1, 2, 3, 6]
b) [1, 2, 3, 1, 2, 3]
c) [2, 4, 6]
d) Error

## Section B: Python Sets (15 Questions)
Q21. Which symbol is used to create a set->
a) []
b) ()
c) {}
d) set[]
Q22. Which of the following is a correct empty set declaration->
a) {}
b) set()
c) Both a and b
d) None
Q23. Are duplicate values allowed in sets->
a) Yes
b) No

c) Only numbers
d) Only strings
Q24. What is the output->
```python
s = {1, 2, 2, 3}

print(s)
```

a) {1, 2, 2, 3}
b) {1, 2, 3}
c) Error
d) None
Q25. Sets in Python are:
a) Ordered
b) Unordered
c) Both
d) None
Q26. Which method is used to add an item to a set->
a) append()
b) add()
c) insert()
d) extend()
Q27. Which method removes an element if present, without raising an error->
a) remove()
b) pop()
c) discard()
d) delete()
Q28. Which operator is used for union of two sets->
a) +
b) |
c) &
d) *
Q29. Which operator is used for intersection of sets->
a) &
b) |
c) -
d) ^
Q30. What will this print->
```python
s = {1, 2, 3}

s.add(2)

print(s)
```

a) {1, 2, 3}
b) {1, 2, 2, 3}
c) Error
d) None
Q31. Which set operation removes duplicates from a list->
a) set(list)
b) list(set)
c) Both a and b
d) None
Q32. What is the output->
```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

print(s1 & s2)
```

a) {1, 2, 3, 4, 5}
b) {3}
c) {1, 2}
d) None
Q33. Which method removes a random element from a set->
a) remove()
b) discard()
c) pop()
d) delete()
Q34. Which operator finds symmetric difference->
a) -
b) ^
c) &
d) |
Q35. What is the output->
```python
s = set("banana")

print(s)
```

a) {'banana'}
b) {'b', 'a', 'n'}
c) ['b', 'a', 'n']
d) Error

## Section C: Python Tuples (15 Questions)
Q36. Which symbol is used to create a tuple->
a) []
b) {}
c) ()
d) <>
Q37. Tuples in Python are:
a) Mutable
b) Immutable
c) Both
d) None
Q38. Which of the following creates a single-element tuple->
a) (5)
b) (5,)
c) [5]
d) {5}
Q39. What is the output->
```python
t = (1, 2, 3)
print(t[1])
```

a) 1
b) 2
c) 3
d) Error
Q40. Which function converts a list into a tuple->
a) tuple()
b) list()
c) set()
d) dict()
Q41. Which method counts occurrences of a value in a tuple->
a) find()
b) count()
c) index()
d) None
Q42. Which method gives index of an element in a tuple->
a) position()
b) count()
c) index()
d) None

## Q43. Can a tuple contain a list->
a) Yes
b) No
c) Only numbers
d) Only strings
Q44. What is the output->
```python
t = (1, 2, [3, 4])
```

t[2][0] = 10
```python
print(t)
```

a) (1, 2, [10, 4])
b) (1, 2, 3, 4)
c) Error
d) None
Q45. Which operation repeats a tuple->
a) *
b) +
c) &
d) ^
Q46. Which of the following is faster->
a) List
b) Tuple
c) Both equal
d) None
Q47. What is the output->
```python
t1 = (1, 2)
t2 = (3, 4)

print(t1 + t2)
```

a) (1, 2, 3, 4)
b) (4, 3, 2, 1)
c) Error
d) None
Q48. What happens if you try t[0] = 5 on a tuple->
a) Updates first element
b) Adds 5 to tuple
c) Error: Tuples are immutable
d) None

## Q49. Which function finds length of a tuple->
a) len()
b) count()
c) size()
d) index()
Q50. Which of these is correct->
a) Tuples use more memory than lists
b) Tuples are immutable, lists are mutable
c) Sets allow duplicates
d) None

## Answer Key
Lists: 1-b, 2-c, 3-b, 4-c, 5-b, 6-a, 7-b, 8-a, 9-c, 10-b,
11-b, 12-b, 13-b, 14-b, 15-a, 16-b, 17-c, 18-b, 19-b, 20-b
Sets: 21-c, 22-b, 23-b, 24-b, 25-b, 26-b, 27-c, 28-b, 29-a, 30-a,
31-c, 32-b, 33-c, 34-b, 35-b
Tuples: 36-c, 37-b, 38-b, 39-b, 40-a, 41-b, 42-c, 43-a, 44-a, 45-a,
46-b, 47-a, 48-c, 49-a, 50-b
