# time: 1
# space: 1

from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        if "0000" in deadends:
            return -1

        def helper(cur_lock):
            res = []
            for i in range(4):
                next_lock0 = cur_lock[0:i] + str((int(cur_lock[i]) + 1) % 10) + cur_lock[i+1:]
                next_lock1 = cur_lock[0:i] + str((int(cur_lock[i]) - 1) % 10) + cur_lock[i+1:]
                if next_lock0 not in visited and next_lock0 not in deadends:
                    res.append(next_lock0)
                    visited.add(next_lock0)

                if next_lock1 not in visited and next_lock1 not in deadends:
                    res.append(next_lock1)
                    visited.add(next_lock1)
            return res

        queue = deque()
        queue.append(('0000',0))
        visited = set('0000')
        while queue: 
            cur_lock, value = queue.popleft()
            if cur_lock == target:
                return value
            next_locks = helper(cur_lock)
            for next_lock in next_locks:
                queue.append((next_lock, value + 1))

        return -1
            

