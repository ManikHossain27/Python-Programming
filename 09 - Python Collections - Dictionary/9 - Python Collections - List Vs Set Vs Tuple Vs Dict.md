# 9 - Python Collections - List Vs Set Vs Tuple Vs Dict

List Vs Set Vs Tuple Vs Dictionary in Python

## Feature List Set Tuple Dictionary
Definition Ordered collection of items Unordered collection of unique items Ordered, immutable
collection of items
Collection of key-value pairs
```python
Syntax list1 = [10, 20, 30] set1 = {10, 20, 30} tuple1 = (10, 20, 30) dict1 = {"a": 1, "b": 2}
```

Order maintained-> Yes No (unordered) Yes Yes (since Python 3.7+)
Indexing supported-> Yes (list1[0]) No Yes (tuple1[1]) Keys can be accessed (dict1["a"])
Mutable (changeable)-> Yes Yes (can add/remove items) No (immutable) Yes
Duplicates allowed-> Yes No (all items must be unique) Yes Keys must be unique (values can
repeat)
Heterogeneous data
allowed->
Yes Yes Yes Yes
Common use cases Store multiple values in
order, can modify
Store unique values, remove duplicates,
fast membership test
Fixed collection of items (like
constants)
Store data as key-value pairs (like a
real-world dictionary)
Example Operations append(), remove(), sort() add(), remove(), union(), intersection() Count, index (tuple.count(),
```python
tuple.index())
keys(), values(), items(), update()
```

## In simple words
- List → Ordered, changeable(mutable), allows duplicates.
- Set → Unordered, unique values only, mutable.
- Tuple → Ordered, unchangeable(immutable), allows duplicates.
- Dictionary → Stores data in key-value pairs, keys must be unique.
