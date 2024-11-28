1.monotonic stack 找每个元素左边第一个比它小的元素位置
储存的stack可以理解为包含远处的最大值，以及稍近一点稍大一点的值，因此能够找到元素左边第一个比他大的值
```python

def monotonic_stack(arr):
    # 初始化结果数组，-1 表示没有比当前元素小的元素
    result = [-1] * len(arr)
    stack = []

    for i in range(len(arr)):
        # 保持单调递增栈，如果栈顶元素比当前元素大，则弹出
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        
        # 如果栈非空，栈顶元素就是左边第一个比当前元素小的元素
        if stack:
            result[i] = stack[-1]
        
        # 当前元素入栈
        stack.append(i)
    
    return result
```
class Solution 

2.有向无环图，topological sort，使用入度和graph作为基本数据结构
```python
from collections import deque

def topological_sort_kahn(graph):
    indegree = {node: 0 for node in graph}  # 初始化入度
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1  # 计算每个节点的入度

    queue = deque([node for node in indegree if indegree[node] == 0])  # 入度为0的节点入队
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1  # 更新相邻节点的入度
            if indegree[neighbor] == 0:
                queue.append(neighbor)  # 入度为0的节点入队

    # 如果拓扑排序的节点数小于图中的节点数，则说明存在环
    if len(topo_order) == len(graph):
        return topo_order
    else:
        return None  # 返回 None 表示图中存在环，无法完成拓扑排序
        
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}
```

3.prefix sum用来计算区间和，以及差分数组操作
```python
# 区间和
nums = [1, 2, 3, 4, 5]
n = len(nums)
prefix = [0] * (n + 1)

# 构建前缀和数组
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + nums[i - 1]

# 计算区间和 [1, 3]（从第 2 个元素到第 4 个元素的和）
l, r = 1, 3
result = prefix[r + 1] - prefix[l]
print(result)  # 输出 9（2 + 3 + 4）

# 差分数组
nums = [0] * 5
diff = [0] * (len(nums) + 1)

# 区间操作：对 [1, 3] 加 2
l, r, k = 1, 3, 2
diff[l] += k
if r + 1 < len(diff):
    diff[r + 1] -= k

# 通过前缀和恢复结果
for i in range(1, len(nums)):
    diff[i] += diff[i - 1]

print(diff[:-1])  # 输出 [0, 2, 2, 2, 0]
```