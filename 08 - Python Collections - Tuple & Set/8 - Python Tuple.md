# 8 - Python Tuple

## Python Collections
(Tuple)

## Tuple
- A tuple is a collection which is:
- Ordered (items have an index).
- Unchangeable (Immutable) (cannot modify, add, or remove items).
- Tuples are written inside round brackets ( ).
Creating a Tuple
```python
mytuple = ("apple", "banana", "cherry")
print(mytuple) # ('apple', 'banana', 'cherry')
```

## Accessing Items
```python
mytuple = ("apple", "banana", "cherry")
print(mytuple[1]) # banana
print(mytuple[-1]) # cherry
```

## Range of Indexes
```python
mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon")
print(mytuple[2:5]) # ('cherry', 'orange', 'kiwi')
print(mytuple[-4:-1]) # ('orange', 'kiwi', 'melon')
```

## Count and Length
```python
mytuple = ("apple", "banana", "apple", "cherry")

print(mytuple.count("apple")) # 2
print(len(mytuple)) # 4
```

## Loop Through a Tuple
```python
mytuple = ("apple", "banana", "cherry")

for item in mytuple
print(item)
```

## Check if Item Exists
```python
mytuple = ("apple", "banana", "cherry")

if "banana" in mytuple
print("Yes, banana exists")
```

## Workaround to Modify a Tuple
Since tuples are immutable, you can convert them to a list, modify, and convert back.
```python
mytuple = ("apple", "banana", "cherry")
temp_list = list(mytuple)
```

temp_list[0] = "orange"
```python
mytuple = tuple(temp_list)
print(mytuple) # ('orange', 'banana', 'cherry')
```

## Joining Tuples
```python
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) # ('a', 'b', 'c', 1, 2, 3)
```

Key Point: Tuples are immutable → once created, they cannot be changed.

### Summary
- List: Mutable (changeable), written with [ ].
- Tuple: Immutable (unchangeable), written with ( ).
- Use lists when you need to update items.
- Use tuples when data should stay constant.
