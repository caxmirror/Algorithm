# time: N*L^2
# space: N*L
class Solution_best:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        L = len(beginWord)
        all_combo_dict = {}
        
        # Preprocess words into intermediate forms
        for word in wordList + [beginWord]:
            for i in range(L):
                intermediate = word[:i] + '*' + word[i+1:]
                if intermediate not in all_combo_dict:
                    all_combo_dict[intermediate] = []
                all_combo_dict[intermediate].append(word)
        
        queue = deque([(beginWord, 1)])
        visited = {beginWord: True}
        
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                intermediate = current_word[:i] + '*' + current_word[i+1:]
                for word in all_combo_dict.get(intermediate, []):
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate] = []
        return 0

# time: n^2
# space: n
class Solution_me:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # shortest
        # BFS? with level counter
        # create a graph, neighbour
        # define helper
        def helper(str1, str2):
            count = 0
            for i in range(len(str1)):
                if str1[i] != str2[i]:
                    count += 1
                    
            if count == 1:
                return True
            return False
    
        neighbours = {}
        if endWord not in wordList:
            return 0
        wordList.extend([beginWord, endWord])
        for word in wordList:
            if word not in neighbours:
                neighbours[word] = []
                for neighbour in neighbours:
                    if helper(neighbour, word):
                        neighbours[word].append(neighbour)
                        neighbours[neighbour].append(word)
        visited = set() # use or not use visited -> used value is going to use again?
        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            node, level = queue.popleft()
            visited.add(node)
            for neighbour in neighbours[node]:
                if neighbour == endWord:
                    return level + 1
                if neighbour not in visited:
                    queue.append((neighbour, level + 1))
        return 0
                