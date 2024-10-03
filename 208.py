class Node:
    def __init__(self):
        self.dic = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur.dic:
                cur.dic[i] = Node()
            cur = cur.dic[i]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur.dic:
                return False
            else:
                cur = cur.dic[i]
        if cur.end == True:
            return True
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.dic:
                return False
            else:
                cur = cur.dic[i]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)