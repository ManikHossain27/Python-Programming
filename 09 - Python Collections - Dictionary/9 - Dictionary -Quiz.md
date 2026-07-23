# 9 - Dictionary -Quiz

## Quiz - Python Dictionary

Q1. Which of the following correctly creates an empty dictionary->
a) d = ()
b) d = []
c) d = {}
d) d = set()

## Q2. What will be the output of
```python
d = {"a": 1, "b": 2}
print(d["a"])
```

a) a
b) 1
c) 2
d) KeyError

Q3. Which method is used to return all keys of a dictionary->
a) d.values()
b) d.keys()
c) d.items()
d) d.get()

Q4. What does len({"x":10, "y":20, "z":30}) return->
a) 2
b) 3
c) 30
d) Error

Q5. Which statement updates the value of key "a" in dictionary d = {"a": 1, "b": 2} to 5->
a) d.update("a":5)
b) d["a"] = 5
c) update(d, "a":5)
d) set(d["a"] = 5)

Q6. What will happen if you access a non-existent key using d["missing"]->
a) Returns None
b) Raises KeyError
c) Creates the key with value None
d) Prints nothing

Q7. Which method allows safe access to dictionary keys without raising an error->
a) d.get("key")
b) d.access("key")
c) d.fetch("key")
d) d.value("key")

## Q8. What will be the output of
```python
d = {"a": 1, "b": 2}

print("c" in d)
```

a) True
b) False
c) c
d) None

Q9. Which method removes a key and returns its value->
a) d.delete()
b) d.remove()
c) d.pop()
d) d.clear()

## Q10. What does d.clear() do->
a) Deletes dictionary variable
b) Removes all key-value pairs
c) Removes last inserted key
d) Raises an error

```python
Q11. What does d = {"a":1}; d2 = d.copy() do->
```

a) Creates a reference to d
b) Creates a shallow copy of d
c) Creates a deep copy of d
d) Deletes d

## Q12. Which method returns key-value pairs as tuples->
a) d.tuple()
b) d.items()
c) d.pairs()
d) d.get()

## Q13. What will be the output of
```python
d = {"x": 1, "y": 2}

for k in d
print(k)
```

a) 1 2
b) x y
c) (x,1) (y,2)
d) Error

Q14. What does dict.fromkeys(["a","b"], 0) create->
a) {'a': None, 'b': None}
b) {'a': 0, 'b': 0}
c) {'a': 'b', 0: 0}
d) Error

Q15. Which method merges another dictionary into the current one->
a) d.append()
b) d.update()
c) d.add()
d) d.merge()

Q16. Which method removes and returns the last inserted key-value pair->
a) d.pop()
b) d.remove()
c) d.popitem()
d) d.last()

## Q17. What is the output->
```python
d = {"a":1, "b":2}
print(d.get("c", 100))
```

a) None
b) 100
c) c
d) Error

## Q18. Which method checks dictionary equality->
a) d.equals(d2)
b) d == d2
c) d.equal(d2)
d) compare(d, d2)

## Q19. What is the output->
```python
d = {"a":{"x":10,"y":20}}
print(d["a"]["y"])
```

a) a
b) y
c) 20
d) Error

Q20. Which method sets a default value if key doesn’t exist->
a) d.setdefault(key, value)
b) d.default(key, value)
c) d.ensure(key, value)
d) d.put(key, value)

Q21. Which of the following is NOT allowed in a dictionary key->
a) String
b) Tuple
c) List
d) Integer
Q22. What is the output->
```python
d = {1:"one", 2:"two"}

print(list(d.values()))
```

a) [1,2]
b) ["one","two"]
c) [(1,"one"), (2,"two")]
d) Error

Q23. What is the default value returned by get() if the key is missing and no default is specified->
a) 0
b) ""
c) None
d) Error

Q24. Which is the correct way to loop through both keys and values->
a)
```python
for k,v in d.items()
print(k,v)
```

b)
```python
for k,v in d
print(k,v)
```

c)
```python
for k,v in d.keys()
print(k,v)
```

d)
```python
for k,v in d.values()
print(k,v)
```

## Q25. What is the output->
```python
d = {"a":1}
d2 = d
```

d2["a"] = 100
```python
print(d["a"])
```

a) 1
b) 100
c) Error
d) None

## Answers
1. c
2. b
3. b
4. b
5. b
6. b
7. a
8. b
9. c
10. b
11. b
12. b
13. b
14. b
15. b
16. c
17. b
18. b
19. c
20. a
21. c
22. b
23. c
24. a
25. b
