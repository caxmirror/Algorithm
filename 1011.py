class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # days combination: 
        l = max(weights)
        r = sum(weights)

        def canShip(load):
            load_remain = load
            days_used = 1
            for i in range(len(weights)):
                if load_remain >= weights[i]:
                    load_remain -= weights[i]
                else:
                    days_used += 1
                    load_remain = load - weights[i]
            if days_used <= days:
                return True
        
        while l < r:
            mid = (l+r)//2
            if canShip(mid):
                r = mid
            else:
                l = mid + 1
        return l



            