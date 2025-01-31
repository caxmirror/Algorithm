# time: N * 2^N
# space:  N * 2^N
class Solution_best:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(left,right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(path, start):
            if start == len(s):
                res.append(path)
                return
            for i in range(start, len(s)):
                if isPalindrome(start,i):
                    backtrack(path + [s[start:i+1]], i+1)
        backtrack([], 0) # convert string to char list
        return res

class Solution_me:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(list_str):
            if list_str == "" or len(list_str)==1:
                return True
            elif list_str[0] == list_str[-1]:

                return isPalindrome(list_str[1:len(list_str)-1])
            else:
                return False
                
        def backtrack(path, options):
            # print(path,options)

            if not options:
                res.append(path)
                return
            for i in range(len(options)):
                if isPalindrome(options[:i+1]):
                    backtrack(path + [options[:i+1]], options[i+1:])
        backtrack([], s) # convert string to char list
        return res