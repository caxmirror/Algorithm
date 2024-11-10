# time: 4^n
# space: M
from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        queue = deque()
        for i,digit in enumerate(digits):
            if i == 0:
                for ch in dic[int(digit)]:
                    queue.append(ch)
            else:
                for i in range(len(queue)):
                    tmp = queue.popleft()
                    for ch in dic[int(digit)]:
                        queue.append(tmp + ch)
        return list(queue)
