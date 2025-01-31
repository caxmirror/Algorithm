# time: k * MlogM
# space: M * n
class Solution_best:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string and then compare
        andagrams = {}
        for string in strs:
            andagram = "".join(sorted(string)) # string sort by char
            # loop of the keys 
            if andagram not in andagrams:
                andagrams[andagram] = [string]
            else:
                andagrams[andagram].append(string)
        return list(andagrams.values())

# time: k * MlogM
# space: M * n
class Solution_best_me:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each string and then compare
        andagrams = {}
        outputs = []
        for string in strs:
            andagram = "".join(sorted(string)) # string sort by char
            # loop of the keys 
            if andagram not in andagrams:
                andagrams[andagram] = len(andagrams) # list unhashable 不能作为dict的key!
                outputs.append([string])
            else:
                outputs[andagrams[andagram]].append(string) #get index form list
        return outputs