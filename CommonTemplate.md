
# Common Algorithms and Patterns in Python

This document covers commonly used algorithms and patterns in Python, useful for competitive programming and coding interviews.

---

### 1. **Binary Search**
```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

def lower_bound(left: int, right: int, P) -> int:
    """
    在闭区间 [left, right] 上二分，找最小的 x 使 P(x) 为真。
    假设答案一定存在。如果不一定, 可以离开二分之后或者进入二分之前检查
若答案可能不存在，在入口或出口加一次检查即可: if !P(right) return -1
    """
    while left < right:                     # 只要区间长度 ≥2 就继续
        mid = (left + right) // 2           # 向下取整
        if P(mid):                          # mid 满足条件，答案 ≤ mid
            right = mid                     # 保留 mid
        else:                               # mid 不满足，答案 > mid
            left = mid + 1
    return left                             # left == right

def upper_bound(left: int, right: int, P) -> int:
    """
    在 [left, right] 上二分，找最大使 P(x) 为真的 x。
    至少保证存在一个可行解。
若答案可能不存在，在入口或出口加一次检查即可: if !P(left) return -1
    """
    while left < right:
        mid = (left + right + 1) // 2 # 要点2!!! 找upper bound右移
        if P(mid):                          # mid 可行，继续右侧找更大
            left = mid + 1                    # 要点1!!! left = mid + 1 lower和upper bound都是这样的
        else:                               # mid 不行，答案 < mid
            right = mid
    return left                         
```

---

### 2. **Two-Pointer Technique**

#### Two-Sum in Sorted Array
```python
def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []  # No solution
```

#### Slow-Fast Pointer for Cycle Detection
```python
def slow_fast_pointer(nums):
    slow, fast = 0, 0
    while fast < len(nums) and fast + 1 < len(nums):
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return True  # Cycle detected
    return False  # No cycle detected
```

---

### 3. **Sliding Window**

#### Fixed-Size Sliding Window for Max Sum
```python
def max_sum_subarray(nums, k):
    max_sum = curr_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        curr_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, curr_sum)
    return max_sum
```

#### Dynamic Sliding Window with Two Pointers
```python
def sliding_window_two_pointers(nums):
    left = 0  # Start of the window

    for right in range(len(nums)):
        # Expand the window by including nums[right] in your calculations

        # Check if the current window meets certain conditions
        while not meets_condition() and left <= right:
            # Shrink the window from the left if it does not meet conditions
            left += 1

        # Update any results based on the current window

    return result  # Return the final result based on the goal
```

---

### 4. **Depth-First Search (DFS)**

#### DFS on Graph
```python
def dfs(graph, start):
    visited = set()
    def helper(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            helper(neighbor)
    helper(start)
    return visited
```

#### DFS for 2D Grid Exploration
```python
def dfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    
    def explore(x, y):
        if (x, y) in visited or x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] == 0:
            return
        visited.add((x, y))
        explore(x + 1, y)
        explore(x - 1, y)
        explore(x, y + 1)
        explore(x, y - 1)

    explore(*start)
    return visited
```

#### DFS for general case
```python
def dfs(state, path, result):
    # Base case: If we reach a desired condition, store the result
    if condition_met(state):
        result.append(path)
        return

    # Recursively explore all possible choices
    for next_state in generate_next_states(state):
        dfs(next_state, path + [next_state], result)

# Helper function to define stopping conditions or constraints
def condition_met(state):
    # Define when to store or stop, e.g., target reached or path length met
    return False

# Helper function to generate possible states or options from the current state
def generate_next_states(state):
    # Define and yield all possible next states or choices from the current state
    yield state

# Main function to start DFS
def solve_problem_with_dfs(initial_state):
    result = []
    dfs(initial_state, [], result)
    return result
```

---

### 5. **Breadth-First Search (BFS)**

#### BFS on Graph
```python
from collections import deque

def bfs(graph, start):
    visited = set([start])
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited
```

#### BFS for 2D Grid Exploration
```python
from collections import deque

def bfs(matrix, start):
    rows, cols = len(matrix), len(matrix[0])
    visited = set([start])
    queue = deque([start])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and matrix[nx][ny] == 1:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return visited
```

#### BFS for general case
# 直接在deque括号内写的collections会被分开成element存到queue中，需要先创建deque，再append
```python
def bfs(initial_state, target_state):
    queue = deque([(initial_state, 0)])  # Each element is (state, depth/steps)
    visited = set([initial_state])       # Track visited states to avoid cycles

    while queue:
        current_state, steps = queue.popleft()

        # Check if we have reached the target
        if current_state == target_state:
            return steps  # Return the number of steps taken to reach the target

        # Generate all possible next states
        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    
    return -1  # Return -1 if the target state is unreachable

# Helper function to define state transitions
def generate_next_states(state):
    # Define and yield all possible states from the current state
    yield state

```
---

### 6. **Backtracking**

#### Permutations
```python
def permute(nums):
    result = []
    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + [options[i]], options[:i] + options[i+1:])
    backtrack([], nums)
    return result
```

---

### 7. **Dynamic Programming (DP)**

#### Fibonacci Sequence (Bottom-Up DP)
```python
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

#### Knapsack Problem
```python
# 0/1 Knapsack  -----------------------
for i in range(N):                  # 依次遍历每件物品
    w, v = weight[i], value[i]
    for j in range(W, w-1, -1):     # **容量 j 逆序递减**
        dp[j] = max(dp[j], dp[j-w] + v)

# Complete Knapsack  ------------------
for i in range(N):
    w, v = weight[i], value[i]
    for j in range(w, W+1):         # **容量 j 正序递增**
        dp[j] = max(dp[j], dp[j-w] + v)

```

---

### 8. **Trie Data Structure**

```python
class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
```

---

### 9. **Greedy Algorithm**

#### Interval Scheduling (Maximum Non-Overlapping Intervals)
```python
def max_meetings(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    count, end_time = 0, float('-inf')
    for start, end in intervals:
        if start >= end_time:
            count += 1
            end_time = end
    return count
```

---

### 10. **Union-Find (Disjoint Set)**

```python
class UnionFind:
    def __init__(self, size):
        self.root = list(range(size))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])  # Path compression
        return self.root[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX  # Union operation
```

---
11.preorder traversal
```python
def preorder_traversal(root: TreeNode) -> List[int]:
    result = []
    def traverse(node):
        if not node:
            return
        result.append(node.val)  # 访问根节点
        traverse(node.left)      # 递归访问左子树
        traverse(node.right)     # 递归访问右子树
    traverse(root)
    return result
# level order traversal
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])  # 初始化队列，将根节点入队

    while queue:
        node = queue.popleft()  # 取出队首节点
        result.append(node.val)
        
        if node.left:
            queue.append(node.left)  # 左子节点入队
        if node.right:
            queue.append(node.right)  # 右子节点入队

    return result

# stack solution preorder
    if not root:
        return []
    
    stack = [root]  # Start with the root node on the stack
    result = []

    while stack:
        # Pop the current node
        current = stack.pop()
        result.append(current.val)  # Visit the node

        # Push right child first so that left is processed first
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    
    return result

# stack solution: inorder
    stack = []
    result = []
    current = root

    while current or stack:
        # Reach the leftmost node of the current subtree
        while current:
            stack.append(current)
            current = current.left

        # Current is None at this point, so backtrack
        current = stack.pop()
        result.append(current.val)  # Process the node (root)

        # Visit the right subtree
        current = current.right
```
---
12.heap
1.如何让heappop出去的元素隔一次再回来(防止连续地输出最大值)
2.do not use nsmallest(), not efficient in time or space

```python
heapq.heapify()
heapq.heappush()
heapq.heappop()
```
Each pattern provides a base template for solving common algorithmic problems effectively and can be adapted to fit specific problem requirements.
