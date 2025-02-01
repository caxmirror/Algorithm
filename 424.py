# time: n
# space: k
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABABBA
        # |   |
        left = 0
        dic = {}
        res = 0
        max_count = 0

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right],0) + 1
            # count max or count the right most?
            max_count = max(max_count, dic[s[right]]) # trick: only need to judge max_count here

            while max_count + k < right - left + 1:
                dic[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res


# time: n(len) * k(unique)
# space: k
class Solution_me:
    def characterReplacement(self, s: str, k: int) -> int:
        # AABABBA
        #   |  |
        # 1.sliding window -> review
            # sliding window: update the result in the final
        # 2.maintain max_count char of the window -> how to(dic and ?)
            # update the max_count is a tough job, can we use something else? only consider the right count is enough
        # 3.condition: max_count + k < right - left + 1
            # we dont need to update maxcount after shirink, they are usually not the good solution

        left = 0
        counts = {}
        res = 0
        for right in range(0, len(s)):
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] += 1
            max_count = 0
            for count in counts:
                max_count = max(max_count,counts[count])
            if max_count + k >= right - left + 1:
                res = max(res, right - left + 1)
            while max_count + k < right - left + 1 and left <= right:
                if counts[s[left]] == 1:
                    del counts[s[left]]
                else:
                    counts[s[left]] -= 1
                left += 1
                max_count = 0
                for count in counts:
                    max_count = max(max_count,counts[count])
        return res