# time: n
# space: u
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        unique = set(nums)
        return len(unique) if 0 not in unique else len(unique) - 1
        
        