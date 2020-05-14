'''
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''


class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.getNode()

    def getNode(self):
        # return a new Instance of TrieNode
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        pCrawl = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])
            if pCrawl.children[index] == None:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pCrawl = self.root
        for i in range(len(word)):
            index = self.charToIndex(word[i])
            if pCrawl.children[index] == None:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pCrawl = self.root
        for i in range(len(prefix)):
            index = self.charToIndex(prefix[i])
            if pCrawl.children[index] == None:
                return False
            pCrawl = pCrawl.children[index]
        return True


if __name__ == '__main__':
    obj = Trie()
    obj.insert('abcd')
    print(obj.search('abcd'))
    print(obj.search('abce'))
    print(obj.startsWith('abc'))
    print(obj.startsWith('abe'))