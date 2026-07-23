# 8 - Python Set

## Python Collections
Set

A set in Python is a collection that has special properties:
- Unordered → Items do not have a fixed position (no indexing).
- Mutable → We can add or remove items (but cannot access or change by index).
- No Duplicates Allowed → Duplicate values are automatically removed.
- Written with curly braces { }.

## Creating a Set
```python
myset1 = {10, 20, 30, 40, 50}
myset2 = {"apple", "mango", "cherry"}
myset3 = {10, "apple", "A", True} # can store mixed data types

myset4 = set() # empty set (use set(), {} creates a dictionary)
```

## Accessing Set Items
- You cannot access items by index (since sets are unordered).
- You cannot update specific items.
- But you can loop through the set.

```python
myset = {"apple", "banana", "cherry"}

for x in myset
print(x)
```

## Check if Item Exists
```python
myset = {"apple", "banana", "cherry"}

print("banana" in myset) # True
print("orange" in myset) # False

if "banana" in myset
print("Yes, banana exists")
```

## Set Functions
```python
myset = {"apple", "banana", "cherry"}
print(len(myset)) # 3 (size of the set)
```

Counting duplicates → Not possible (since duplicates don’t exist).
Sorting / Reversing → Not possible (since set is unordered).

## Adding Items
- add() → adds a single item
- update() → adds multiple items
```python
myset = {"apple", "banana", "cherry"}

myset.add("orange")
print(myset) # {'banana', 'apple', 'orange', 'cherry'}

myset.update(["mango", "grapes"])
print(myset) # {'banana', 'apple', 'cherry', 'grapes', 'orange', 'mango'}
```

## Removing Items
1. remove(value) → removes item, error if not found.
2. discard(value) → removes item, no error if not found.
3. pop() → removes a random item.
```python
myset = {"apple", "banana", "cherry"}

myset.remove("banana")
print(myset) # {'apple', 'cherry'}

myset.discard("xyz") # No error even if item not present
myset.pop() # removes random item

print(myset)
```

## Clear / Delete a Set
```python
myset = {"apple", "banana", "cherry"}

myset.clear()
print(myset) # set() → empty set

del myset
```

```python
# print(myset) # NameError (set is deleted)
```

## Copying a Set
```python
myset1 = {"apple", "banana", "cherry"}

myset2 = myset1.copy() # Approach 1
myset3 = set(myset1) # Approach 2

print(myset2)
print(myset3)
```

## Joining Two Sets
1. Union → Combines all items from both sets
```python
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) # {'a', 'b', 'c', 1, 2, 3}
```

### 2. Intersection → Returns only common items
```python
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3) # {'apple'}
```

### Summary
- Set is Unordered → No indexing, sorting, or reversing.
- Mutable → You can add or remove items.
- No Duplicates → Each item is unique.
