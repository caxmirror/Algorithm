# time: m + n
# space: m + n
class Solution_best_me:
    def minWindow(self, s: str, t: str) -> str:
        # chars need to be included in s
        # 
        # 1.dic store count in the window
        # 2.shrink the window if overly meet condition
        # 3.dic, dic_target
        # 3.meet condition: sum of elements in dic_target == count, update count each time
        left = 0
        count = 0
        dic = {}
        dic_target = {}
        res_count = float("inf")
        res = ""

        for ch in t:
            dic_target[ch] = dic_target.get(ch, 0) + 1
            count += 1

        for right in range(len(s)):
            dic[s[right]] = dic.get(s[right], 0) + 1
            if dic[s[right]] <= dic_target.get(s[right],0):
                count -= 1

            while dic[s[left]] > dic_target.get(s[left],0) and left < right:
                dic[s[left]] -= 1
                left += 1

            if res_count > right - left + 1 and count == 0:
                res = s[left:right + 1]
                res_count = right - left + 1
        return res
