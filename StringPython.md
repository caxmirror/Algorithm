
# String Manipulation Techniques in Python

This guide covers a variety of useful string manipulation techniques and methods in Python, especially helpful for solving problems on platforms like LeetCode.

---

### 1. **Basic String Search and Matching**

#### `str.find(substring)`
```python
# Returns the index of the first occurrence of substring. If not found, returns -1.
s = "hello world"
index = s.find("world")  # 6
```

#### `str.index(substring)`
```python
# Similar to find(), but raises a ValueError if the substring is not found.
s = "hello world"
index = s.index("world")  # 6
```

#### `str.rfind(substring)` and `str.rindex(substring)`
```python
# Searches for the last occurrence of substring.
s = "hello world world"
last_index = s.rfind("world")  # 12
```

#### `str.startswith(prefix)` and `str.endswith(suffix)`
```python
# Checks if a string starts or ends with a given substring.
s = "hello world"
s.startswith("hello")  # True
s.endswith("world")    # True
```

---

### 2. **Counting and Replacing Characters**

#### `str.count(substring)`
```python
# Counts the number of non-overlapping occurrences of a substring.
s = "hello world world"
count = s.count("world")  # 2
```

#### `str.replace(old, new, count)`
```python
# Replaces occurrences of old with new. Optional count limits the replacements.
s = "hello world world"
s_replaced = s.replace("world", "everyone")  # "hello everyone everyone"
```

---

### 3. **String Case Manipulation**

#### `str.lower()` and `str.upper()`
```python
# Converts the string to lowercase or uppercase.
s = "Hello World"
s.lower()  # "hello world"
s.upper()  # "HELLO WORLD"
```

#### `str.capitalize()` and `str.title()`
```python
# capitalize() capitalizes the first letter of the string. title() capitalizes the first letter of each word.
s = "hello world"
s.capitalize()  # "Hello world"
s.title()       # "Hello World"
```

---

### 4. **String Splitting and Joining**

#### `str.split(delimiter, maxsplit=-1)`
```python
# Splits a string into a list using delimiter. If delimiter is not specified, it splits by whitespace.
s = "hello world everyone"
words = s.split()           # ['hello', 'world', 'everyone']
limited_split = s.split(" ", 1)  # ['hello', 'world everyone']
```

#### `str.rsplit(delimiter, maxsplit=-1)`
```python
# Splits from the right side, which can be useful in some cases.
s = "hello world everyone"
words = s.rsplit(" ", 1)    # ['hello world', 'everyone']
```

#### `str.join(iterable)`
```python
# Joins elements of an iterable into a single string with the specified delimiter.
words = ["hello", "world"]
sentence = " ".join(words)  # "hello world"
```

---

### 5. **Trimming Whitespace**

#### `str.strip()`, `str.lstrip()`, and `str.rstrip()`
```python
# strip() removes whitespace (or specified characters) from both ends. lstrip() and rstrip() remove from the left or right end, respectively.
s = "   hello world   "
s.strip()      # "hello world"
s.lstrip()     # "hello world   "
s.rstrip()     # "   hello world"
```

---

### 6. **Character Conversion**

#### `ord(char)` and `chr(num)`
```python
# ord(char) converts a character to its Unicode code, and chr(num) converts a Unicode code to its character.
ord('a')  # 97
chr(97)   # 'a'
```

#### `str.translate()` and `str.maketrans()`
```python
# Used for character-by-character replacements.
s = "hello world"
trans_table = str.maketrans("hwe", "HWE")
s_translated = s.translate(trans_table)  # "HEllo World"
```

---

### 7. **String Alignment**

#### `str.center(width, fillchar=' ')`, `str.ljust(width, fillchar=' ')`, `str.rjust(width, fillchar=' ')`
```python
# Centers, left-justifies, or right-justifies the string with optional fill characters.
s = "hello"
s.center(10, '-')  # "--hello---"
s.ljust(10, '-')   # "hello-----"
s.rjust(10, '-')   # "-----hello"
```

---

### 8. **Checking for Alphanumeric Properties**

#### `str.isdigit()`, `str.isalpha()`, `str.isalnum()`, etc.
```python
# isdigit(): Checks if all characters are digits.
# isalpha(): Checks if all characters are alphabetic.
# isalnum(): Checks if all characters are alphanumeric (letters or numbers).
s = "12345"
s.isdigit()  # True

s = "abc"
s.isalpha()  # True

s = "abc123"
s.isalnum()  # True
```

---

### 9. **Reversing Strings**

#### Using Slicing
```python
# s[::-1] reverses the string by slicing with a negative step.
s = "hello"
reversed_s = s[::-1]  # "olleh"
```

