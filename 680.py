# time: n
# space: 1
class Solution_me:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        count = 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else: 
                count -= 1
                cur_left = left + 1
                cur_right = right
                while cur_left < cur_right and s[cur_left] == s[cur_right]:
                    cur_left += 1
                    cur_right -= 1
                if cur_left >= cur_right:
                    return True

                cur_left = left
                cur_right = right - 1
                while cur_left < cur_right and s[cur_left] == s[cur_right]:
                    cur_left += 1
                    cur_right -= 1
                if cur_left >= cur_right:
                    return True
                else: 
                    return False
        return True