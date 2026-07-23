# 15 - File Handling - Part1

## Python File Handling

File handling in Python allows us to create, read, write, update, and delete files and
directories.
The open() function is the most commonly used to work with files.

## Opening a File
```python
file = open("filename.txt", "mode")
```

## File Modes
- 'r' → Read (default). File must exist.
- 'w' → Write. Creates a new file if not exists, overwrites existing content.
- 'a' → Append. Creates a new file if not exists, adds content at the end without
overwriting.
- 'x' → Create. Creates a new file but raises an error if the file already exists.

## Writing to a File
Example: Using open() with w mode
```python
file = open("C:\\Automation\\automationFiles\\myfile.txt", 'w')

file.write("Welcome to Python \nFile Handling")
file.close()
```

### Example: Using with statement
```python
with open("C:\\Automation\\automationFiles\\myfile.txt", 'w') as file:
```

```python
file.write("Welcome to Python \nFile Handling")
```

- The with statement automatically closes the file after use.

## Appending Data to a File
```python
file = open("C:\\Automation\\automationFiles\\myfile.txt", 'a')

file.write("\nThis line is appended.")
file.close()
```

Note: Unlike write mode (w), append mode (a) does not delete old content.

## Reading from a File
There are multiple ways to read

```python
file = open("C:\\Automation\\automationFiles\\myfile.txt", 'r')
content = file.read() # Reads the entire file

print(content)
```

```python
# file.readline() → Reads one line at a time
# file.readlines() → Reads all lines into a list
```

```python
file.close()
```

## Renaming a File
```python
import os
sourcefile = "C:\\Automation\\automationFiles\\myfile.txt"
targetfile = "C:\\Automation\\automationFiles\\myfile1.txt"

os.rename(sourcefile, targetfile)
print("File renamed")
```

## Deleting a File
```python
import os

file = "C:\\Automation\\automationFiles\\myfile1.txt"

if os.path.exists(file)

os.remove(file)
else
print("File does not exist")
```

## Creating a Directory
```python
import os

os.mkdir("C:\\Automation\\automationFiles\\mydir")
print("Directory created")
```

## Checking if a Directory Exists
```python
import os
dir_name = "C:\\Automation\\automationFiles\\mydir"

if os.path.exists(dir_name)
print("Directory exists")

else
print("Directory does not exist")
```

## Renaming a Directory
```python
import os

sourcedir = "C:\\Automation\\automationFiles\\mydir"
targetdir = "C:\\Automation\\automationFiles\\mydir1"

os.rename(sourcedir, targetdir)
print("Directory renamed")
```

## Removing a Directory
```python
import os

os.rmdir("C:\\Automation\\automationFiles\\mydir1")
print("Directory removed")
```

### Note
```python
os.rmdir() only removes empty directories.
```

## For non-empty folders, use
```python
import shutil

shutil.rmtree("folder_name")
```

## Get Current Working Directory
```python
import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")
```
