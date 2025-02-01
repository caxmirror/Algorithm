# time: len(pile) * log max(pile)
# space: 1

class Solution_best:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1.greedy / math

        # 2.dp

        # 3.binary search
        # 3.1 sort(no need in this problem!)
        # 3.2 left = min elem, right = max elem
        # 3.3 condition: if time > h, return False

        left = 1
        right = max(piles)
        res = right

        def condition(k):
            time = 0
            for pile in piles:
                time += ceil(pile / k)
            return time <= h

        while left <= right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res



# time: nlogn + len(pile) * log max(pile)
# space: 1
class Solution_me:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1.greedy / math

        # 2.dp

        # 3.binary search
        # 3.1 sort(no need in this problem!)
        # 3.2 left = min elem, right = max elem
        # 3.3 condition: if time > h, return False

        piles.sort() # nlogn, no need 
        left = 1
        right = piles[-1]
        res = right

        def condition(k):
            time = 0
            for pile in piles:
                time += ceil(pile / k)
            return time <= h

        while left <= right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid - 1
                res = mid
            else:
                left = mid + 1
        return res
