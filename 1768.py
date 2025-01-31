# time: m + n
# space: m + n
class Solution_best:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        min_len = min(m, n)
        merged_word = []
        for i in range(min_len):
            merged_word.append(word1[i])
            merged_word.append(word2[i])
        if m > n:
            merged_word.extend(word1[n:])
        else:
            merged_word.extend(word2[m:])
        return "".join(merged_word)

# time: m + n
# space: (m + n)^2
class Solution_me:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_word = ""
        m = len(word1)
        n = len(word2)
        min_len = min(m, n)
        for i in range(min_len):
            merged_word += word1[i] + word2[i]
        if m > n:
            merged_word += word1[n:]
        else:
            merged_word += word2[m:]
        return merged_word

        

