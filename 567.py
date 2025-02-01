# time: n
# space: n
class Solution_best:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1.sliding window
        # 2.fixed window size = len(s1)
        # 3.store all characters of s1: dic_s1
        # 4.store all characters of window: dic_window
        # 5.condition: use count of dic_s1 to avoid repeat, update cound when slide window

        # eidboaoo
        #     ||
        # ab

        dic_s1 = {}
        for ch in s1:
            dic_s1[ch] = dic_s1.get(ch, 0) + 1
        dic_window = {} 
        left = 0 
        for right in range(len(s2)): 
            dic_window[s2[right]] = dic_window.get(s2[right], 0) + 1 
            if right - left >= len(s1): 
                dic_window[s2[left]] -= 1
                if dic_window[s2[left]] == 0:
                    del dic_window[s2[left]]
                left += 1
            if dic_window == dic_s1: # 可以直接判断两个dic内容相同
                return True 
        return False

# time: n
# space: n
class Solution_best_me:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1.sliding window
        # 2.fixed window size = len(s1)
        # 3.store all characters of s1: dic_s1
        # 4.store all characters of window: dic_window
        # 5.condition: use count of dic_s1 to avoid repeat, update cound when slide window
        # eidboaoo
        #     ||
        # ab

        dic_s1 = {}
        count = 0 # the element in dic_s1
        for ch in s1:
            dic_s1[ch] = dic_s1.get(ch, 0) + 1
            count += 1

        dic_window = {}
        left = 0
        for right in range(len(s2)):
            dic_window[s2[right]] = dic_window.get(s2[right], 0) + 1
            if dic_window[s2[right]] <= dic_s1.get(s2[right],0):
                count -= 1
            if right - left >= len(s1):
                dic_window[s2[left]] -= 1
                if dic_window[s2[left]] < dic_s1.get(s2[left],0):
                    count += 1
                left += 1
            if count == 0:
                return True
        return False