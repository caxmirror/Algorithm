# time: n + m
# space: n + m
class Solution_best_me:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        VOWEL = set(['a','i','o','u','e'])
        def starts_ends_with_vowel(s):
            if s[0] in VOWEL and s[-1] in VOWEL:
                return 1
            else:
                return 0
        n = len(words)
        prefix_sum = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i-1] + starts_ends_with_vowel(words[i-1]) # check
        m = len(queries)
        result = []
        for i in range(m):
            result.append(prefix_sum[queries[i][1] + 1] - prefix_sum[queries[i][0]])
        return result

