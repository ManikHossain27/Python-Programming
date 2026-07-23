# 9 - Python Dictionary

## Python Dictionary
A dictionary in Python is a collection of data stored in key : value pairs.
Properties of a dictionary
- Ordered (from Python 3.7+) – items maintain insertion order.
- Mutable (Changeable) – we can add, update, or remove items.
- Indexed by keys – values are accessed using keys (not positions).
- No duplicate keys – each key must be unique.
- Written using curly braces { }.

### 1. Creating a Dictionary
Approach 1: Using {}
```python
mydic = {"brand": "Ford", "model": "Aspire", "year": 2024}
```

## Approach 2: Using dict() constructor
```python
mydic = dict(name="John", age=36, country="Norway")
```

## Values can be of any data type
```python
mydic = {
```

"brand": "Ford",
"electric": True,
"year": 2025,
"colors": ["red", "white", "blue"]
}

### 2. Accessing Items
- Using key name
```python
print(mydic["model"]) # Aspire
```

- Using get() method
```python
print(mydic.get("model")) # Aspire
```

### 3. Get Keys
```python
print(mydic.keys()) # dict_keys(['brand', 'model', 'year'])
```

### 4. Get Values
```python
print(mydic.values()) # dict_values(['Ford', 'Aspire', 2024])
```

### 5. Get Items (Key-Value Pairs)
```python
print(mydic.items()) # dict_items([('brand', 'Ford'), ('model', 'Aspire'), ('year', 2024)])
```

### 6. Check if a Key Exists
```python
if "model" in mydic
print("Yes, exists")
```

### 7. Adding Items
mydic["color"] = "red"
```python
print(mydic)
```

```python
# {'brand': 'Ford', 'model': 'Aspire', 'year': 2025, 'color': 'red'}
```

### 8. Updating Items
```python
mydic.update({"color": "white"})
mydic.update({"year": 2026})
```

### 9. Removing Items
- pop(key) → removes specific key
```python
mydic.pop("model")
```

- popitem() → removes the last inserted item (random in <3.7)
```python
mydic.popitem()
```

- del keyword → removes a specific key or the entire dictionary
```python
del mydic["model"] # remove key

del mydic # delete dictionary
```

- clear() → empties dictionary
```python
mydic.clear()
```

### 10. Copying a Dictionary
- Using copy()
```python
mydic2 = mydic.copy()
```

- Using dict()
```python
mydic2 = dict(mydic)
```

### 11. Looping Through a Dictionary
```python
mydic = {"brand": "Ford", "model": "Aspire", "year": 2025}
```

```python
# Loop through keys
```

```python
for key in mydic
print(key)
```

```python
# Loop through values
```

```python
for value in mydic.values()
print(value)
```

```python
# Loop through key-value pairs
```

```python
for key, value in mydic.items()
print(key, value)
```

### Summary
- A dictionary stores data in key : value pairs.
- Keys are unique; values can be any type.
- Ordered (3.7+), Mutable, Indexed by keys.
- Supports many useful methods: .keys(), .values(), .items(), .get().
- Great for storing structured data (like JSON).
