
# Practical LeetCode Python Functions and Manipulations

### 1. **List Manipulations**

#### Sorting a List
```python
nums = [3, 1, 4, 1, 5]
nums.sort()  # Sorts in-place, ascending order
# or
sorted_nums = sorted(nums, reverse=True)  # Creates a new sorted list in descending order
```

#### Finding Min/Max
```python
min_val = min(nums)
max_val = max(nums)
```

#### Slicing Lists
```python
subarray = nums[1:4]  # Slices from index 1 to 3 (4 is exclusive)
```

#### List Comprehension
```python
squares = [x*x for x in nums if x > 2]  # Squares only numbers greater than 2
```

#### List Sum and Product
```python
total_sum = sum(nums)
```

---

### 2. **String Manipulations**

#### Splitting and Joining Strings
```python
s = "hello world"
words = s.split()  # Splits by whitespace
joined_string = " ".join(words)  # Joins list into a single string with spaces
```

#### Checking for Substrings
```python
s = "leetcode"
contains = "leet" in s  # True if "leet" is a substring
```

#### Reversing a String
```python
reversed_s = s[::-1]  # Slicing to reverse
```

#### Converting Case
```python
s_lower = s.lower()
s_upper = s.upper()
```

---

### 3. **Dictionary Manipulations**

#### Counting Frequency of Elements
```python
from collections import Counter

nums = [1, 2, 2, 3, 3, 3]
frequency = Counter(nums)  # Returns a dictionary-like Counter object
# frequency: {1: 1, 2: 2, 3: 3}
```

#### Accessing and Setting Default Values
```python
dict_example = {}
value = dict_example.get('key', 0)  # Returns 0 if 'key' does not exist

# Using defaultdict for automatic default values
from collections import defaultdict
dict_example = defaultdict(int)
dict_example['key'] += 1  # Initializes 'key' with 0 and increments
```

#### Sorting a Dictionary by Key or Value
```python
sorted_by_key = dict(sorted(frequency.items()))
sorted_by_value = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
```

---

### 4. **Set Operations**

#### Basic Set Operations
```python
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b      # Union of two sets
intersection_set = set_a & set_b  # Intersection of two sets
difference_set = set_a - set_b  # Difference of two sets
```

#### Removing Duplicates from a List
```python
unique_nums = list(set(nums))  # Convert to set to remove duplicates, then back to list
```

---

### 5. **Heap (Priority Queue)**

```python
import heapq

nums = [3, 1, 4, 1, 5]
heapq.heapify(nums)  # Turns list into a min-heap in-place

# Getting the smallest elements
smallest = heapq.heappop(nums)  # Pops the smallest item
k_smallest = heapq.nsmallest(3, nums)  # Gets the 3 smallest items
k_largest = heapq.nlargest(3, nums)

# Using max heap by inverting values
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
largest = -heapq.heappop(max_heap)  # Pops the largest item by inverting back
```

---

### 6. **Deque for Sliding Window**

```python
from collections import deque

window = deque()
window.append(1)        # Add element to the right end
window.appendleft(2)    # Add element to the left end
window.pop()            # Remove element from the right end
window.popleft()        # Remove element from the left end
```

---

### 7. **Math and Logic Operations**

#### Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
```python
import math

gcd_val = math.gcd(8, 12)  # Returns 4
lcm_val = abs(8 * 12) // gcd_val  # LCM formula using GCD
```

#### Power and Square Root
```python
power = pow(2, 3)  # 2^3 = 8
square_root = math.sqrt(16)  # 4.0
```

#### Modulo for Large Numbers
```python
result = (a * b) % MOD  # Commonly used in large number problems to keep values manageable
```

---

### 8. **Common Functional Programming Helpers**

#### Using `map`, `filter`, and `reduce`
```python
nums = [1, 2, 3, 4]

# Apply a function to each item
squared = list(map(lambda x: x*x, nums))  # [1, 4, 9, 16]

# Filter items based on a condition
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

# Reduce to a single value (sum of squares)
from functools import reduce
sum_squares = reduce(lambda x, y: x + y*y, nums, 0)  # 30
```

---

### 9. **Built-in Itertools for Combinations and Permutations**

```python
from itertools import permutations, combinations, product

# All permutations of length 2
perm = list(permutations(nums, 2))  # Returns all possible ordered pairs

# All combinations of length 2
comb = list(combinations(nums, 2))  # Returns all possible pairs without repetition

# Cartesian product of two lists
prod = list(product([1, 2], ['a', 'b']))  # [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]
```

---

### 10. **Enumerate for Index-Based and Parallel Iteration**

#### Enumerate for Index-Based Iteration
```python
for i, num in enumerate(nums):
    print(i, num)  # Prints index and element
```

### 11. **Basic Type Conversion Functions**

#### `int(x, base=10)`
```python
# Converts x to an integer. Optional base allows converting from binary, octal, etc.
int('10')      # 10
int('1010', 2) # 10 (binary to decimal)
```

#### `float(x)`
```python
# Converts x to a floating-point number.
float('3.14')  # 3.14
```

#### `str(x)`
```python
# Converts x to a string.
str(123)       # '123'
```

#### `ord(char)`
```python
# Returns the Unicode code of a character.
ord('a')       # 97
```

#### `chr(num)`
```python
# Converts a Unicode code to its character.
chr(97)        # 'a'
```

---

### 12. **Explanation of `functools.lru_cache`**

The `lru_cache` decorator is a built-in caching mechanism in Python that allows you to store the results of expensive function calls and reuse them when the function is called with the same arguments, effectively reducing computation time.

#### Example with Fibonacci
```python
from functools import lru_cache

@lru_cache(None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

1. **Caching with `@lru_cache(None)`**: Here, `None` sets the cache size to unlimited. A `maxsize` can also be specified to limit the cache.

2. **Recursive Fibonacci Calculation**: This function calls itself recursively to calculate the nth Fibonacci number. With `lru_cache`, each unique input is cached to avoid redundant calculations.

3. **Efficiency Gain**: Without `lru_cache`, calculating `fibonacci(n)` requires recalculating values multiple times, making it very inefficient (exponential time complexity). With caching, each Fibonacci number is computed only once, turning the complexity into \(O(n)\).

This caching strategy can be highly effective for problems involving repeated calculations or overlapping subproblems, such as dynamic programming.

13.4种取整函数 
```python
math.floor() == //; 
math.ceil()==// + 1; 
round(); 
int()  #toward 0
```

